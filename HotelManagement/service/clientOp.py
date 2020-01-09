from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QTableWidgetItem

from service import globalValue
from ui.client import Ui_MainWindow
from dao.dbOpClient import Client

class ClientOp(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(ClientOp, self).__init__(parent)
        self.setupUi(self)
        self.staff = globalValue.get_staff()
        self.welcome.setText(self.staff.sname)
        self.role.setText('权限：'+ self.staff.srole)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.searchNB.clicked.connect(self.searchClient)
        self.commitAdd.clicked.connect(self.addClient)
        self.commitAddT.clicked.connect(self.addTeam)
        self.tableDelB.clicked.connect(self.tableDel)

    def searchClient(self):
        if self.typeC.isChecked():
            type = '个人'
        elif self.typeT.isChecked():
            type = '团队'
        else:
            QMessageBox().information(None, "提示", "必须选择一种方式！", QMessageBox.Yes)
            return False
        name = self.searchName.text()
        if name == '':
            name = "%%"
        times = self.searchTimes.text()
        print(times)
        if times == '':
            times = 0
        times = int(times)
        c = Client()
        data = c.findClient(type,name,times)
        if type == '个人':
            self.tableClient.setHorizontalHeaderLabels(['姓名', '身份证', '手机号','年龄','性别','注册员工编号','入住次数','注册时间'])
        elif type == '团队':
            self.tableClient.setHorizontalHeaderLabels(['团队名称','团队标识','团队预留手机号','登记员工编号','入住次数','注册时间'])
        if len(data) == 0:
            QMessageBox().information(None,"提示","没有满足要求的客户",QMessageBox.Yes)
            return False
        rowNum = len(data)
        columnNum = len(data[0])
        self.tableClient.setRowCount(rowNum)
        self.tableClient.setColumnCount(columnNum)
        for i, da in enumerate(data):
            da = list(da.values())
            for j in range(columnNum):
                self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                self.tableClient.setItem(i, j, self.itemContent)

    def tableDel(self):
        if self.typeC.isChecked():
            type = '个人'
        elif self.typeT.isChecked():
            type = '团队'
        else:
            QMessageBox().information(None, "提示", "必须选择一种方式！", QMessageBox.Yes)
            return False
        row_selected = self.tableClient.selectedItems()
        if len(row_selected) == 0:
            return
        row = row_selected[0].text()
        c = Client()
        c.tableDelDB(type,row)
        row = row_selected[0].row()
        self.tableClient.removeRow(row)
        QMessageBox().information(None, "提示", "删除成功！", QMessageBox.Yes)

    def addTeam(self):
        tname = self.tname.text()
        tid = self.tid.text()
        tphone = self.tphone.text()
        c = Client()
        if c.addTeamDB(tname,tid,tphone):
            QMessageBox.information(None, '提示', '添加成功', QMessageBox.Yes)
        else:
            QMessageBox.information(None, '提示', '数据已存在', QMessageBox.Yes)

    def addClient(self):
        cname = self.cname.text()
        cage = self.cage.text()
        if self.cmale.isChecked():
            csex = '男'
        elif self.cfemale.isChecked():
            csex = '女'
        else:
            QMessageBox.information(None,'提示','请选择性别',QMessageBox.Yes)
        cid = self.cid.text()
        cphone = self.cphone.text()
        c = Client()
        if c.addClientDB(cname,cid,cphone,cage,csex):
            QMessageBox.information(None, '提示', '添加成功', QMessageBox.Yes)
        else:
            QMessageBox.information(None, '提示', '数据已存在', QMessageBox.Yes)


