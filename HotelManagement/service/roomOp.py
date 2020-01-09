from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QTableWidgetItem,QVBoxLayout, QLabel,QPushButton
from ui.room import Ui_MainWindow
from dao.dbOpRoom import Room
from service import globalValue
import datetime


class RoomOp(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(RoomOp, self).__init__(parent)
        self.setupUi(self)
        self.staff = globalValue.get_staff()
        self.welcome.setText(self.staff.sname)
        self.role.setText('权限：'+ self.staff.srole)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.inputStartTime.setCalendarPopup(True)
        self.inputEndTime.setCalendarPopup(True)
        self.endtime.setCalendarPopup(True)
        self.tendtime.setCalendarPopup(True)
        self.starttime_booking.setCalendarPopup(True)
        self.endtime_booking.setCalendarPopup(True)
        self.tstarttime_booking.setCalendarPopup(True)
        self.tendtime_booking.setCalendarPopup(True)
        self.starttime_checkout.setCalendarPopup(True)
        self.endtime_checkout.setCalendarPopup(True)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_sub.setCurrentIndex(0)
        self.stackedWidget_sub_2.setCurrentIndex(0)
        self.stackedWidget_sub_3.setCurrentIndex(0)
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listWidget_2.currentRowChanged.connect(self.stackedWidget_sub.setCurrentIndex)
        self.listWidget_3.currentRowChanged.connect(self.stackedWidget_sub_2.setCurrentIndex)
        self.listWidget_4.currentRowChanged.connect(self.stackedWidget_sub_3.setCurrentIndex)
        self.commitCheckin.clicked.connect(self.singleCheckin)
        self.commitCheckinTeam.clicked.connect(self.teamCheckin)
        self.commitBookingClient.clicked.connect(self.reserveClient)
        self.commitBookingTeam.clicked.connect(self.reserveTeam)
        self.commitDeBookC.clicked.connect(self.cancelReserveC)
        self.commitDeBookT.clicked.connect(self.cancelReserveT)
        self.commitCheckout.clicked.connect(self.checkout)
        self.searchNB.clicked.connect(self.showRoomInfo)
        self.commitTableDel.clicked.connect(self.tableDel)
        self.commitTableModify.clicked.connect(self.tableModify)
        self.commitAddRoom.clicked.connect(self.addRoom)
        self.commitrtcC.clicked.connect(self.reverseToCheckC)
        self.commitrtcT.clicked.connect(self.reverseToCheckT)
        self.commitSearch.clicked.connect(self.findRoom)
        self.scan.clicked.connect(self.setBrowerPath)
        self.reset.clicked.connect(self.reOpen)

    # 下面用布局的方式显示房间
    def showRoom(self,rid,rtype,rstorey,rprice,rdesc,rpic,endtime,i,j):
        self.glayout = self.gridLayout
        self.glayout.setContentsMargins(10,3,10,3)
        # 下面展示信息
        self.flayout = QVBoxLayout()
        self.glayout.addLayout(self.flayout,i,j)
        lb = QLabel(self)
        lb.setFixedSize(150,80)
        lb.setPixmap(QPixmap(rpic))
        lb.setStyleSheet("border:1px solid white")
        lb.setScaledContents(True)
        self.flayout.addWidget(lb)
        self.flayout.addWidget(QLabel("房间号:"+rid + "    楼层:"+rstorey,self, styleSheet="color: #990066;"))
        self.flayout.addWidget(QLabel("类型:"+rtype, self, styleSheet="color: #990066;", openExternalLinks=True))
        self.flayout.addWidget(QLabel("描述:"+rdesc+" 价格:"+rprice, self, styleSheet="color: #990066;", openExternalLinks=True))
        pb = QPushButton(self)
        pb.setFixedSize(80,25)
        pb.setText("立即订购")
        pb.setStyleSheet("background:#CCFFCC;border-radius:8px;\n")
        self.flayout.addWidget(pb)
        pb.clicked.connect(lambda: self.pbSwitch(rid,endtime))

    def reOpen(self):
        self.close()
        self.tmp = RoomOp()
        self.tmp.show()

    def findRoom(self):
        rtype = self.inputType.currentText()
        if rtype == '请选择...':
            rtype = '%%'
        print(rtype)
        if self.inputFree.isChecked():
            rstate = 1
        else:
            rstate = 0
        rstorey = self.inputstorey.currentText()
        if rstorey == '请选择...':
            rstorey = '%%'
        rstarttime = self.inputStartTime.date().toPyDate()
        rendtime = self.inputEndTime.date().toPyDate()
        if rendtime <= rstarttime:
            QMessageBox().information(None, "提示", "结束时间必须大于开始时间！", QMessageBox.Yes)
            return False
        price_bottom = self.inputprice1.text()
        if price_bottom == '':
            price_bottom = 0
        price_up = self.inputprice2.text()
        if price_up == '':
            price_up = 10000
        r = Room()
        da = r.showRoom(rtype,rstate,rstorey,rstarttime,rendtime,price_bottom,price_up)
        length = len(da)
        if length == 0:
            QMessageBox().information(None, "提示", "没有符合要求的记录！", QMessageBox.Yes)
            return False
        k = 0
        for i in range(1 + int(length / 3)):
            for j in range(3):
                if k == length:
                    break
                print(k)
                self.showRoom(da[k]['rid'],da[k]['rtype'],da[k]['rstorey'],da[k]['rprice'],da[k]['rdesc'],da[k]['rpic'],rendtime,i,j)
                k = k + 1
        return True




    def pbSwitch(self,rid,endtime):
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_sub.setCurrentIndex(0)
        self.crid.setText(rid)
        self.endtime.setDate(endtime)

    def singleCheckin(self):
        cname = self.cname.text()
        cid = self.cid.text()
        cphone = self.cphone.text()
        cage = self.cage.text()
        if self.male.isChecked():
            csex = '男'
        elif self.female.isChecked():
            csex = '女'
        else:
            csex = ''
        crid = self.crid.text()
        endtime = self.endtime.date().toPyDate()
        if endtime <= datetime.date.today():
            QMessageBox().information(None, "提示", "结束时间必须大于今天！", QMessageBox.Yes)
            return False
        remark = self.remark.text()
        r = Room()
        ret = r.singleCheckinDB(cname,cid,cphone,cage,csex,crid,endtime,remark)
        if ret:
            QMessageBox().information(None, "提示", "入住信息登记完成！", QMessageBox.Yes)

    def teamCheckin(self):
        tname = self.tname.text()
        tid = self.tid.text()
        tphone = self.tphone.text()
        trid = self.trid.text()
        tendtime = self.tendtime.date().toPyDate()
        if tendtime <= datetime.date.today():
            QMessageBox().information(None, "提示", "结束时间必须大于今天！", QMessageBox.Yes)
            return False
        tremark = self.tremark.text()
        r = Room()
        print(tid)
        ret = r.teamCheckinDB(tname, tid, tphone,trid,tendtime,tremark)
        if ret:
            QMessageBox().information(None, "提示", "入住信息登记完成！", QMessageBox.Yes)

    def reverseToCheckC(self):
        cid = self.cid_rtc.text()
        rid = self.crid_rtc.text()
        r = Room()
        ret = r.reserveToCheckinC(cid,rid)
        if ret == True:
            QMessageBox().information(None, "提示", "预约入住完成！", QMessageBox.Yes)


    def reverseToCheckT(self):
        tid = self.tid_rtc.text()
        rid = self.trid_rtc.text()
        print(tid,rid)
        r = Room()
        ret = r.reserveToCheckinT(tid, rid)
        if ret:
            QMessageBox().information(None, "提示", "预约入住完成！", QMessageBox.Yes)

    def reserveClient(self):
        cname = self.cname_booking.text()
        cid = self.cid_booking.text()
        cphone = self.cphone_booking.text()
        cage = self.cage_booking.text()
        if self.male_booking.isChecked():
            csex = '男'
        elif self.female_booking.isChecked():
            csex = '女'
        else:
            csex = ''
        crid = self.crid_booking.text()
        cstarttime = self.starttime_booking.date().toPyDate()
        cendtime = self.endtime_booking.date().toPyDate()
        if cendtime <= cstarttime:
            QMessageBox().information(None, "提示", "结束时间必须大于开始时间！", QMessageBox.Yes)
            return False
        cremark = self.remark_booking.text()
        r = Room()
        ret = r.reserveCDB(cname,cid,cphone,cage,csex,crid,cstarttime,cendtime,cremark)
        if ret:
            QMessageBox().information(None, "提示", "预约信息登记完成！", QMessageBox.Yes)

    def reserveTeam(self):
        tname = self.tname_booking.text()
        tid = self.tid_booking.text()
        tphone = self.tphone_booking.text()
        trid = self.trid_booking.text()
        tstarttime = self.tstarttime_booking.date().toPyDate()
        tendtime = self.tendtime_booking.date().toPyDate()
        if tendtime <= tstarttime:
            QMessageBox().information(None, "提示", "结束时间必须大于开始时间！", QMessageBox.Yes)
            return False
        tremark = self.tremark_booking.text()
        r = Room()
        ret = r.reserveTDB(tname,tid,tphone,trid,tstarttime,tendtime,tremark)
        if ret:
            QMessageBox().information(None, "提示", "预约信息登记完成！", QMessageBox.Yes)

    def cancelReserveC(self):
        cancel_cid = self.cid_deb.text()
        cancel_rid = self.crid_deb.text()
        r = Room()
        ret = r.cancelReserveCDB(cancel_cid,cancel_rid)
        if ret:
            QMessageBox().information(None, "提示", "取消预约成功！", QMessageBox.Yes)

    def cancelReserveT(self):
        cancel_tid = self.tid_deb.text()
        cancel_rid = self.trid_deb.text()
        r = Room()
        ret = r.cancelReserveTDB(cancel_tid,cancel_rid)
        if ret:
            QMessageBox().information(None, "提示", "取消预约成功！", QMessageBox.Yes)

    def checkout(self):
        id = self.id_checkout.text()
        if self.single_flag.isChecked():
            check_type = '个人'
        elif self.team_flag.isChecked():
            check_type = '团队'
        else:
            messageBox = QMessageBox()
            messageBox.setWindowTitle('错误')
            messageBox.setText('必须选择个人/团队')
            messageBox.exec_()
            return
        stime = self.starttime_checkout.date().toPyDate()
        etime = self.endtime_checkout.date().toPyDate()
        if etime <= stime:
            QMessageBox().information(None, "提示", "结束时间必须大于开始时间！", QMessageBox.Yes)
            return False
        rid = self.rid_checkout.text()
        pay_type = self.paytype_checkout.text()
        remark = self.remark_checkout.text()
        r = Room()
        ret = r.checkoutDB(check_type,id,rid,pay_type,remark)
        if ret:
            QMessageBox().information(None, "提示", "退房成功！", QMessageBox.Yes)

    def showRoomInfo(self):
        r = Room()
        if int(self.staff.srole) > 1:
            data = r.showAllRoom()
            print(data)
            rowNum = len(data)
            columnNum = len(data[0])
            self.roomTable.setRowCount(rowNum)
            self.roomTable.setColumnCount(columnNum)
            for i,da in enumerate(data):
                da = list(da.values())
                for j in range(columnNum):
                    self.itemContent = QTableWidgetItem(( '%s' )  % (da[j]))
                    self.roomTable.setItem(i, j, self.itemContent)
        else:
            QMessageBox().information(None, "提示", "权限要求不符合！", QMessageBox.Yes)

    def tableDel(self):
        row_selected = self.roomTable.selectedItems()
        if len(row_selected) == 0:
            return
        row = row_selected[0].text()
        r = Room()
        r.delRoom(row)
        row = row_selected[0].row()
        self.roomTable.removeRow(row)
        QMessageBox().information(None, "提示", "删除成功！", QMessageBox.Yes)

    def tableModify(self):
        row_selected = self.roomTable.selectedItems()
        if len(row_selected) == 0:
            return
        row = row_selected[0].row()
        column  = row_selected[0].column()
        value = self.modifyvalue.text()
        r = Room()
        r.modifyRoom(row,column,value)
        tvalue = QTableWidgetItem(('%s') % (value))
        self.roomTable.setItem(row,column, tvalue)
        QMessageBox().information(None, "提示", "修改成功！", QMessageBox.Yes)

    def addRoom(self):
        if int(self.staff.srole) > 1:
            rid = self.rid_add.text()
            rtype = self.rtype_add.currentText()
            rstorey = self.rstorey_add.currentText()
            rprice = self.rprice_add.text()
            rdesc = self.rdesc_add.text()
            rpic = self.path.text()
            r = Room()
            ret = r.addRoom(rid,rtype,rstorey,rprice,rdesc,rpic)
            if ret == True:
                QMessageBox().information(None, "提示", "添加房源成功！", QMessageBox.Yes)
        else:
            QMessageBox().information(None, "提示", "权限不符合要求！", QMessageBox.Yes)

    def setBrowerPath(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self,"选择图片路径","D:\pictures")
        self.path.setText(download_path)





