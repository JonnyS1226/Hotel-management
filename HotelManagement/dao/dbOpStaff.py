import pymysql
from PyQt5.QtWidgets import QMessageBox
from dao.dbConfig import localSourceConfig as localConfig

class Staff:
    """
    员工操作类
    """
    def __init__(self, config=localConfig):
        self.db = pymysql.connect(host=config['host'],port=config['port'],user=config['user'],
                                      passwd=config['passwd'],db=config['db'],charset=config['charset'],
                                      cursorclass=config['cursorclass'])
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print("Database version : %s " % data['VERSION()'])
        self.username = None
        self.password = None
        self.srole = None
        self.sid = None
        self.sname = None
        self.ssex = None
        self.stime = None
        self.sidcard = None
        self.sphone = None

    def userLogin(self, username, password):
        """
        员工登录操作
        :return: row[6]：员工权限    或False：登录失败
        """
        try:
            self.cursor.execute("select * from staff")
            data = self.cursor.fetchall()
            for row in data:
                if row['susername'] == username and row['spassword'] == password:
                    self.username = username
                    self.password = password
                    self.sid = row['sid']
                    self.sname = row['sname']
                    self.ssex = row['ssex']
                    self.stime = row['stime']
                    self.srole = row['srole']
                    self.sidcard = row['sidcard']
                    self.sphone = row['sphone']
                    return row['srole']
        except Exception as e:
            print(e)
            return False

    def modifyPasswd(self, sid, newPasswd, oldPasswd):
        """员工登录后修改密码"""

        try:
            self.cursor.execute("select * from staff where sid=%s ", (sid))
            data = self.cursor.fetchall()[0]
            if data['spassword'] == oldPasswd:
                self.cursor.execute("update staff set spassword=%s where sid=%s ",(newPasswd, sid))
                self.db.commit()
                self.password = newPasswd
                print("ok")
                return True
            else:
                print("no")
                return False
        except Exception as e:
            print(e)
            return False

    def forgetPasswd(self, newPasswd,sid,sidcard):
        """员工登录时忘记密码，使用身份证找回"""
        try:
            self.cursor.execute("select * from staff where sid=%s",sid)
            data = self.cursor.fetchall()[0]
            print(data)
            if data['sidcard'] == sidcard:
                self.cursor.execute("update staff set spassword=%s where sid=%s",(newPasswd,sid))
                self.db.commit()
                self.password = newPasswd
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def addStaff(self,sid,sname,ssex,stime,susername,spassword,srole,sidcard,sphone):
        """管理者增加员工"""
        try:
            self.cursor.execute("insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sid,sname,ssex,stime,susername,spassword,srole,sidcard,sphone))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            QMessageBox().information(None, "提示", "该员工已存在！", QMessageBox.Yes)
            return False

    def showAllStaff(self,sname):
        """管理者查看员工"""
        try:
            self.cursor.execute("select * from staff where sname like %s",(sname))
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(e)
            return False

    def deleteStaff(self,sid,sname,sidcard):
        """管理者删除员工信息"""
        try:
            self.cursor.execute("delete from staff where sid=%s and sname=%s and sidcard=%s",(sid,sname,sidcard))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            QMessageBox().information(None, "提示", "没有相关员工信息！", QMessageBox.Yes)
            return False

    def delStaff(self,sid):
        """表格上直接删除"""
        try:
            self.cursor.execute("delete from staff where sid=%s",(sid))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def modifyStaff(self, row, column, value):
        """表格上直接修改"""
        # 字典方法得到要修改的列
        SQL_COLUMN = ['sid','sname','ssex','stime','susername','spassword','srole','sidcard','sphone']
        try:
            self.cursor.execute("select * from staff")
            data = self.cursor.fetchall()
            rid_selected = data[row]['rid']
            sql = "update room set " + SQL_COLUMN[column] + "='" + value + "'where rid='" + rid_selected +"'"
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False




