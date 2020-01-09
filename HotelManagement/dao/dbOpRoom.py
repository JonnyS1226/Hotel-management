import pymysql
from dao.dbConfig import localSourceConfig as localConfig
from PyQt5.QtWidgets import QMessageBox
from service import globalValue
import datetime
import re

class Room:
    """客房信息操作类"""
    def __init__(self,config=localConfig):
        self.db = pymysql.connect(host=config['host'],port=config['port'],user=config['user'],
                                      passwd=config['passwd'],db=config['db'],charset=config['charset'],
                                      cursorclass=config['cursorclass'])
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print("Database version : %s " % data['VERSION()'])
        self.staff = globalValue.get_staff()

    def showAllRoom(self):
        self.cursor.execute("select * from room")
        data = self.cursor.fetchall()
        return data

    def showRoom(self,rtype,rstate,rstorey,rstarttime,rendtime,price_bottom,price_up):
        """根据条件检索房间"""
        print(rstarttime, rendtime)
        if rstate == 0:
            self.cursor.execute("select * from room where rtype like %s and rstorey like %s and rprice between %s and %s",
                            (rtype,rstorey,int(price_bottom),int(price_up)))
            data1 = self.cursor.fetchall()
            return data1
        elif rstate == 1:
            self.cursor.execute(
                "select rid from room where rtype like %s and rstorey like %s and rprice between %s and %s",
                (rtype, rstorey, int(price_bottom), int(price_up)))
            data = self.cursor.fetchall()
            list_data = []
            for i in range(len(data)):
                crid = data[i]['rid']
                self.cursor.execute(
                    "select * from checkin_client as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                    "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>=%s or A.start_time>=%s and A.end_time<=%s)"
                    , (crid, rstarttime, rstarttime, rendtime, rendtime, rstarttime, rendtime,rstarttime,rendtime))
                data1 = self.cursor.fetchall()
                self.cursor.execute(
                    "select * from checkin_team as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                    "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>=%s or A.start_time>=%s and A.end_time<=%s)"
                    , (crid, rstarttime, rstarttime, rendtime, rendtime, rstarttime, rendtime,rstarttime,rendtime))
                data2 = self.cursor.fetchall()
                self.cursor.execute(
                    "select * from booking_client as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                    "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>=%s or A.start_time>=%s and A.end_time<=%s)"
                    , (crid, rstarttime, rstarttime, rendtime, rendtime, rstarttime, rendtime,rstarttime,rendtime))
                data3 = self.cursor.fetchall()
                self.cursor.execute(
                    "select * from booking_team as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                    "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>=%s or A.start_time>=%s and A.end_time<=%s)"
                    , (crid, rstarttime, rstarttime, rendtime, rendtime, rstarttime, rendtime,rstarttime,rendtime))
                data4 = self.cursor.fetchall()
                if data1 == () and data2 == () and data3 == () and data4 == ():
                    list_data.append(crid)
            ret = []
            for i in range(len(list_data)):
                rid_ret = list_data[i]
                self.cursor.execute("select * from room where rid=%s",(rid_ret))
                ret = ret + self.cursor.fetchall()
            return ret

    def addRoom(self,rid,rtype,rstorey,rprice,rdesc,rpic):
        """增加房间"""
        try:
            self.cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s)",(rid,rtype,rstorey,rprice,rdesc,rpic))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            QMessageBox().information(None, "提示", "房间号已存在！", QMessageBox.Yes)
            return False

    def delRoom(self,rid):
        """表格上直接删除"""
        try:
            self.cursor.execute("delete from room where rid=%s",(rid))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def modifyRoom(self, row, column, value):
        """表格上直接修改"""
        # 字典方法得到要修改的列
        SQL_COLUMN = ['rid','rtype','rstorey','rprice','rdesc']
        try:
            self.cursor.execute("select * from room")
            data = self.cursor.fetchall()
            rid_selected = data[row]['rid']
            sql = "update room set " + SQL_COLUMN[column] + "='" + value + "'where rid='" + rid_selected +"'"
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def singleCheckinDB(self,cname,cid,cphone,cage,csex,crid,cendtime,remark):
        """个人入住"""
        # 查询预定表和入住表，判断该房间是否能租出去
        starttime = datetime.date.today()
        self.cursor.execute("select * from checkin_client as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                            "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>=%s or A.start_time>=%s and A.end_time<=%s)"
                            ,(crid,starttime,starttime,cendtime,cendtime,starttime,cendtime,starttime,cendtime))
        data1 = self.cursor.fetchall()
        self.cursor.execute("select * from checkin_team as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                            "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>=%s or A.start_time>=%s and A.end_time<=%s)"
                            , (crid, starttime, starttime, cendtime, cendtime, starttime, cendtime,starttime,cendtime))
        data2 = self.cursor.fetchall()
        self.cursor.execute("select * from booking_client as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                            "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>=%s or A.start_time>=%s and A.end_time<=%s)"
                            , (crid, starttime, starttime, cendtime, cendtime, starttime, cendtime,starttime,cendtime))
        data3 = self.cursor.fetchall()
        self.cursor.execute("select * from booking_team as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                            "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>=%s or A.start_time>=%s and A.end_time<=%s)"
                            , (crid, starttime, starttime, cendtime, cendtime, starttime, cendtime,starttime,cendtime))
        data4 = self.cursor.fetchall()
        if data1 != () or data2 != () or data3 != () or data4 != ():
            QMessageBox().information(None, "提示", "该时间段对应房间被占用（入住/预约）！", QMessageBox.Yes)
            return False
        self.cursor.execute("select * from client where cid=%s",(cid))
        data = self.cursor.fetchall()
        if data == ():
            self.cursor.execute("insert into client(cname,cid,cphone,cage,csex,register_sid,accomodation_times) "
                                "values(%s,%s,%s,%s,%s,%s,%s)",(cname,cid,cphone,cage,csex,self.staff.sid,0))
        self.cursor.execute("select * from room where rid=%s",(crid))
        data = self.cursor.fetchall()
        if data == ():
            QMessageBox().information(None, "提示", "没有对应房间号！", QMessageBox.Yes)
            return False
        perPrice = data[0]['rprice']
        totalPrice = int(perPrice) * int((cendtime-starttime).days)
        try:
            self.cursor.execute("insert into checkin_client values(%s,%s,%s,%s,%s,%s,%s)",
                                (crid,cid,starttime,cendtime,totalPrice,self.staff.sid,remark))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            QMessageBox().information(None, "提示", "相关客户已入住，请勿重复插入", QMessageBox.Yes)
            return False

    def teamCheckinDB(self,tname,tid,tphone,ttrid,tendtime,tremark):
        """团体入住"""
        tstarttime = datetime.date.today()
        for trid in re.split(',|，| ', ttrid):
            print(trid)
            self.cursor.execute(
                "select * from checkin_client as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                "or A.end_time>%s and A.start_time<=%s or A.start_time<=%s and A.end_time>=%s or A.start_time>=%s and A.end_time<=%s)"
                , (trid, tstarttime, tstarttime, tendtime, tendtime, tstarttime, tendtime, tstarttime, tendtime))
            data1 = self.cursor.fetchall()
            print(data1)
            self.cursor.execute("select * from checkin_team as A where (A.rid=%s) and ((A.end_time>%s and A.start_time<%s) "
                                "or (A.end_time>%s and A.start_time<%s) or (A.start_time<=%s and A.end_time>=%s) or (A.start_time>=%s and A.end_time<=%s))"
                                , (trid, tstarttime, tstarttime, tendtime, tendtime, tstarttime, tendtime, tstarttime, tendtime))
            data2 = self.cursor.fetchall()
            print(data2)
            self.cursor.execute(
                "select * from booking_client as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>=%s or A.start_time>=%s and A.end_time<=%s)"
                , (trid, tstarttime, tstarttime, tendtime, tendtime, tstarttime, tendtime, tstarttime, tendtime))
            data3 = self.cursor.fetchall()
            print(data3)
            self.cursor.execute("select * from booking_team as A where (A.rid=%s) and ((A.end_time>%s and A.start_time<%s) "
                                "or (A.end_time>%s and A.start_time<%s) or (A.start_time<=%s and A.end_time>=%s) or (A.start_time>=%s and A.end_time<=%s))"
                                , (trid, tstarttime, tstarttime, tendtime, tendtime, tstarttime, tendtime, tstarttime, tendtime))
            data4 = self.cursor.fetchall()
            print(data4)
            if data1 != () or data2 != () or data3 != () or data4 != ():
                QMessageBox().information(None, "提示", "该时间段对应房间被占用（入住/预约）！", QMessageBox.Yes)
                return False
        try:
            for i in re.split(',|，| ', ttrid):
                self.cursor.execute("select * from team where tid=%s", (tid))
                data = self.cursor.fetchall()
                if data == ():
                    self.cursor.execute("insert into team(tname,tid,tphone,check_in_sid,accomodation_times) values(%s,%s,%s,%s,%s)",
                                        (tname, tid, tphone, self.staff.sid, 0))

                self.cursor.execute("select * from room where rid=%s",(i))
                perPrice = self.cursor.fetchall()[0]['rprice']
                starttime = datetime.date.today()
                totalPrice = int(perPrice) * int((tendtime - starttime).days)
                self.cursor.execute("insert into checkin_team values(%s,%s,%s,%s,%s,%s,%s)",
                                    (i, tid, starttime, tendtime, totalPrice, self.staff.sid, tremark))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def reserveToCheckinC(self,cid,rid):
        """个人预约订单入住"""
        # 先查找预约表
        starttime = datetime.date.today()
        self.cursor.execute("select * from booking_client where cid=%s and rid=%s and start_time=%s",(cid,rid,starttime))
        data = self.cursor.fetchall()
        if data == ():
            QMessageBox().information(None, "提示", "没有对应预约或者预约入住时间未到！", QMessageBox.Yes)
            return False
        # 再从预约表中获取相关信息
        endtime = data[0]['end_time']
        remark = data[0]['remark']
        # 下面计算房价
        self.cursor.execute("select * from room where rid=%s",(rid))
        data = self.cursor.fetchall()
        if data == ():
            QMessageBox().information(None, "提示", "没有对应房间号！", QMessageBox.Yes)
            return False
        perPrice = data[0]['rprice']
        totalPrice = int(perPrice) * int((endtime-starttime).days)
        try:
            self.cursor.execute("insert into checkin_client values(%s,%s,%s,%s,%s,%s,%s)",
                                (rid,cid,starttime,endtime,totalPrice,self.staff.sid,remark))
            self.cursor.execute("delete from booking_client where cid=%s and rid=%s and start_time=%s",(cid,rid,starttime))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False


    def reserveToCheckinT(self,tid,rrid):
        """团队预定入住"""
        starttime = datetime.date.today()
        for rid in re.split(',|，| ', rrid):
            print(rid)
            self.cursor.execute("select * from booking_team where tid=%s and rid=%s and start_time=%s",
                                (tid, rid, starttime))
            data = self.cursor.fetchall()
            print(data)
            if data == ():
                QMessageBox().information(None, "提示", "%s房间没有对应预约或者预约入住时间未到！"%rid, QMessageBox.Yes)
                return False
            # 再从预约表中获取相关信息
            endtime = data[0]['end_time']
            remark = data[0]['remark']
            # 下面计算房价
            self.cursor.execute("select * from room where rid=%s", (rid))
            data = self.cursor.fetchall()
            if data == ():
                QMessageBox().information(None, "提示", "没有%s房间号！"%rid, QMessageBox.Yes)
                return False
            perPrice = data[0]['rprice']
            totalPrice = int(perPrice) * int((endtime - starttime).days)
            try:
                self.cursor.execute("insert into checkin_team values(%s,%s,%s,%s,%s,%s,%s)",
                                    (rid, tid, starttime, endtime, totalPrice, self.staff.sid, remark))
                self.cursor.execute("delete from booking_team where tid=%s and rid=%s and start_time=%s",
                                    (tid, rid, starttime))
                self.db.commit()
            except Exception as e:
                print(e)
                return False
        return True

    def reserveCDB(self,cname,cid,cphone,cage,csex,crid,cstarttime,cendtime,cremark):
        """个人预约"""
        starttime = datetime.date.today()
        self.cursor.execute("select * from checkin_client as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                            "or A.end_time>%s and A.start_time<%s A.start_time<=%s and A.end_time>%s or A.start_time>=%s and A.end_time<=%s)"
                            , (crid, starttime, starttime, cendtime, cendtime, starttime, cendtime, starttime, cendtime))
        data1 = self.cursor.fetchall()
        self.cursor.execute("select * from checkin_team as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                            "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>%s or A.start_time>=%s and A.end_time<=%s)"
                            , (crid, starttime, starttime, cendtime, cendtime, starttime, cendtime, starttime, cendtime))
        data2 = self.cursor.fetchall()
        self.cursor.execute("select * from booking_client as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                            "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>%s or A.start_time>=%s and A.end_time<=%s)"
                            , (crid, starttime, starttime, cendtime, cendtime, starttime, cendtime, starttime, cendtime))
        data3 = self.cursor.fetchall()
        self.cursor.execute("select * from booking_team as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                            "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>%s or A.start_time>=%s and A.end_time<=%s)"
                            , (crid, starttime, starttime, cendtime, cendtime, starttime, cendtime, starttime, cendtime))
        data4 = self.cursor.fetchall()
        if data1 != () or data2 != () or data3 != () or data4 != ():
            QMessageBox().information(None, "提示", "该时间段对应房间被占用（入住/预约）！", QMessageBox.Yes)
            return False
        self.cursor.execute("select * from client where cid=%s",(cid))
        data = self.cursor.fetchall()
        if data == ():
            self.cursor.execute(
                "insert into client(cname,cid,cphone,cage,csex,register_sid,accomodation_times) values(%s,%s,%s,%s,%s,%s,%s)",
                (cname, cid, cphone, cage, csex, self.staff.sid, 0))
        try:
            self.cursor.execute("insert into booking_client(cid,rid,start_time,end_time,remark) values(%s,%s,%s,%s,%s)",
                                (cid,crid,cstarttime,cendtime,cremark))
            self.db.commit()
            return  True
        except Exception as e:
            print(e)
            QMessageBox().information(None, "提示", "相关预约信息已存在！", QMessageBox.Yes)
            return False

    def reserveTDB(self,tname,tid,tphone,ttrid,tstarttime,tendtime,tremark):
        """团体预约"""
        for trid in re.split(',|，| ', ttrid):
            self.cursor.execute(
                "select * from checkin_client as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>%s or A.start_time>=%s and A.end_time<=%s)"
                , (trid, tstarttime, tstarttime, tendtime, tendtime, tstarttime, tendtime, tstarttime, tendtime))
            data1 = self.cursor.fetchall()
            self.cursor.execute("select * from checkin_team as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                                "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>%s or A.start_time>=%s and A.end_time<=%s)"
                                , (trid, tstarttime, tstarttime, tendtime, tendtime, tstarttime, tendtime, tstarttime, tendtime))
            data2 = self.cursor.fetchall()
            self.cursor.execute(
                "select * from booking_client as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>%s or A.start_time>=%s and A.end_time<=%s)"
                , (trid, tstarttime, tstarttime, tendtime, tendtime, tstarttime, tendtime, tstarttime, tendtime))
            data3 = self.cursor.fetchall()
            self.cursor.execute("select * from booking_team as A where (A.rid=%s) and (A.end_time>%s and A.start_time<%s "
                                "or A.end_time>%s and A.start_time<%s or A.start_time<=%s and A.end_time>%s or A.start_time>=%s and A.end_time<=%s)"
                                , (trid, tstarttime, tstarttime, tendtime, tendtime, tstarttime, tendtime, tstarttime, tendtime))
            data4 = self.cursor.fetchall()
            if data1 != () or data2 != () or data3 != () or data4 != ():
                QMessageBox().information(None, "提示", "该时间段对应房间被占用（入住/预约）！", QMessageBox.Yes)
                return False
            self.cursor.execute("select * from team where tid=%s", (tid))
            data = self.cursor.fetchall()
            if data == ():
                self.cursor.execute(
                    "insert into team(tname,tid,tphone,check_in_sid,accomodation_times) values(%s,%s,%s,%s,%s)",
                    (tname, tid, tphone, self.staff.sid, 0))
            try:
                self.cursor.execute("insert into booking_team(tid,rid,start_time,end_time,remark) values(%s,%s,%s,%s,%s)",
                                    (tid, trid, tstarttime, tendtime, tremark))
                self.db.commit()
            except Exception as e:
                print(e)
                QMessageBox().information(None, "提示", "相关预约信息已存在！", QMessageBox.Yes)
                return False
        return True

    def cancelReserveCDB(self,cancel_cid,cancel_rid):
        """个人取消预约"""
        self.cursor.execute("select * from booking_client where cid=%s and rid=%s",(cancel_cid,cancel_rid))
        if self.cursor.fetchall() == ():
            QMessageBox().information(None, "提示", "没有相关预约信息！", QMessageBox.Yes)
            return False
        try:
            self.cursor.execute("delete from booking_client where cid=%s and rid=%s",(cancel_cid,cancel_rid))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            QMessageBox().information(None, "提示", "没有相关预约信息！", QMessageBox.Yes)
            return False

    def cancelReserveTDB(self,cancel_tid,cancel_rid):
        """团体取消预约"""
        try:
            for r in re.split(',|，| ', cancel_rid):
                self.cursor.execute("select * from booking_team where tid=%s and rid=%s", (cancel_tid, r))
                if self.cursor.fetchall() == ():
                    QMessageBox().information(None, "提示", "%s房间没有预约！"%r, QMessageBox.Yes)
                    return False
                self.cursor.execute("delete from booking_team where tid=%s and rid=%s",(cancel_tid,r))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def checkoutDB(self,flag, id,rid,payType,remark):
        """两种方式退房"""
        try:
            if flag == '个人':
                self.cursor.execute("select * from checkin_client where rid=%s and cid=%s",(rid,id))
                data = self.cursor.fetchall()
                if data == ():
                    QMessageBox().information(None, "提示", "没有相关入住信息！", QMessageBox.Yes)
                    return False
                else:
                    rid_out = data[0]['rid']
                    cid_out = data[0]['cid']
                    stime_out = data[0]['start_time']
                    etime_out = data[0]['end_time']
                    money = data[0]['total_price']
                    self.cursor.execute("insert into hotelorder(id,ordertype,start_time,end_time,rid,pay_type,money,remark,register_sid) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (cid_out,flag,stime_out,etime_out,rid_out,payType,money,remark,self.staff.sid))
                    self.cursor.execute("delete from checkin_client where rid=%s and cid=%s",(rid_out,cid_out))
                    self.db.commit()
                    QMessageBox().information(None, "提示", "本次需要支付%s" %money, QMessageBox.Yes)
            elif flag == '团队':
                sum = 0
                for r in re.split(',|，| ',rid):
                    self.cursor.execute(
                        "select * from checkin_team where rid=%s and tid=%s", (r, id))
                    data = self.cursor.fetchall()
                    if data == ():
                        QMessageBox().information(None, "提示", "没有相关入住信息！", QMessageBox.Yes)
                        return False
                    else:
                        rid_out = data[0]['rid']
                        tid_out = data[0]['tid']
                        stime_out = data[0]['start_time']
                        etime_out = data[0]['end_time']
                        money = data[0]['total_price']
                        self.cursor.execute(
                            "insert into hotelorder(id,ordertype,start_time,end_time,rid,pay_type,money,remark,register_sid) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            , (tid_out, flag, stime_out, etime_out, rid_out, payType, money, remark,self.staff.sid))
                        self.cursor.execute("delete from checkin_team where rid=%s and tid=%s", (rid_out, tid_out))
                        self.db.commit()
                        sum = sum + int(money)
                QMessageBox().information(None, "提示", "本次需要支付%s" %str(sum), QMessageBox.Yes)
            return True
        except Exception as e:
            print(e)
            return False






if __name__ == '__main__':
    global staff
    staff = globalValue._initStaff('zs123','123456')
    staff.userLogin()
    r = Room()
    # r.checkoutDB('团队','30','201，205','1','2')
    # r.checkoutDB('个人','23233','406','1','2')
    r.modifyRoom(1,1,'222')

