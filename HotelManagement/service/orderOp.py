
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QTableWidgetItem
from ui.order import Ui_MainWindow
from dao.dbOpOrder import Order
from service import globalValue


class OrderOp(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(OrderOp, self).__init__(parent)
        self.setupUi(self)
        self.staff = globalValue.get_staff()
        self.welcome.setText(self.staff.sname)
        self.role.setText('权限：'+ self.staff.srole)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.stackedWidget.setCurrentIndex(0)
        self.searchNB.clicked.connect(self.searchBooking)
        self.searchorderB.clicked.connect(self.searchOrder)
        self.searchCheckinB.clicked.connect(self.searchCheckin)

    def searchCheckin(self):
        if self.typeC_2.isChecked():
            type = '个人'
        elif self.typeT_2.isChecked():
            type = '团队'
        else:
            QMessageBox().information(None, "提示", "必须选择个人还是团队方式！", QMessageBox.Yes)
            return False
        id = self.searchName_2.text()
        if id == '':
            id = '%%'
        rid = self.searchRid_2.text()
        if rid == '':
            rid = '%%'
        o = Order()
        data = o.findCheckin(type,id,rid)
        if len(data) == 0:
            QMessageBox().information(None, "提示", "没有满足要求的记录！", QMessageBox.Yes)
            return False
        if type == '个人':
            self.tableCheckin.setHorizontalHeaderLabels(['房间号', '身份证', '开始时间','结束时间','总待付金额','登记入住的员工编号','备注'])
        elif type == '团队':
            self.tableCheckin.setHorizontalHeaderLabels(['房间号','团队标识','开始时间','结束时间','总待付金额','登记入住的员工编号','备注'])
        rowNum = len(data)
        columnNum = len(data[0])
        self.tableCheckin.setRowCount(rowNum)
        self.tableCheckin.setColumnCount(columnNum)
        for i, da in enumerate(data):
            da = list(da.values())
            for j in range(columnNum):
                self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                self.tableCheckin.setItem(i, j, self.itemContent)

    def searchBooking(self):
        if self.typeC.isChecked():
            type = '个人'
        elif self.typeT.isChecked():
            type = '团队'
        else:
            QMessageBox().information(None, "提示", "必须选择个人还是团队方式！", QMessageBox.Yes)
            return False
        id = self.searchName.text()
        if id == '':
            id = '%%'
        rid = self.searchRid.text()
        if rid == '':
            rid = '%%'
        o = Order()
        data = o.findBooking(type,id,rid)
        if len(data) == 0:
            QMessageBox().information(None, "提示", "没有满足要求的记录！", QMessageBox.Yes)
            return False
        if type == '个人':
            self.tableBooking.setHorizontalHeaderLabels(['身份证', '房间号', '开始时间','结束时间','预定时间','备注'])
        elif type == '团队':
            self.tableBooking.setHorizontalHeaderLabels(['团队标识','房间号','开始时间','结束时间','预定时间','备注'])
        rowNum = len(data)
        columnNum = len(data[0])
        self.tableBooking.setRowCount(rowNum)
        self.tableBooking.setColumnCount(columnNum)
        for i, da in enumerate(data):
            da = list(da.values())
            for j in range(columnNum):
                self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                self.tableBooking.setItem(i, j, self.itemContent)

    def searchOrder(self):
        id = self.ordername.text()
        if id == '':
            id = '%%'
        money = self.ordermoney.text()
        if money == '':
            money = '0'
        rid = self.orderrid.text()
        if rid == '':
            rid = '%%'
        o = Order()
        data = o.findOrder(id,money,rid)
        self.tableOrder.setHorizontalHeaderLabels(['用户标识', '用户形式', '开始时间', '结束时间', '房间号','支付方式','支付金额','备注','订单时间','办理的员工编号'])
        rowNum = len(data)
        columnNum = len(data[0])
        self.tableOrder.setRowCount(rowNum)
        self.tableOrder.setColumnCount(columnNum)
        for i, da in enumerate(data):
            da = list(da.values())
            for j in range(columnNum):
                self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                self.tableOrder.setItem(i, j, self.itemContent)
