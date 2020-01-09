
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QTableWidgetItem
from ui.staff import Ui_MainWindow
from service import globalValue


class StaffOP(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(StaffOP, self).__init__(parent)
        self.setupUi(self)
        self.inputdate.setCalendarPopup(True)
        self.stackedWidget.setCurrentIndex(0)
        self.staff = globalValue.get_staff()
        self.welcome.setText(self.staff.sname)
        self.role.setText('权限：'+ self.staff.srole)
        self.name.setText(self.staff.sname)
        self.sname.setText(self.staff.sname)
        self.ssex.setText(self.staff.ssex)
        self.srole.setText(self.staff.srole)
        self.stime.setText(str(self.staff.stime))
        self.sphone.setText(self.staff.sphone)
        self.sidcard.setText(self.staff.sidcard)
        self.sidcard_2.setText(self.staff.sid)
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 绑定事件
        self.searchNB.clicked.connect(self.searchStaff)
        self.commitAdd.clicked.connect(self.addStaff)
        self.commitDe.clicked.connect(self.deleteStaff)
        self.commitTableDel.clicked.connect(self.tableDel)
        self.commitTableModify.clicked.connect(self.tableModify)

    def searchStaff(self):
        sname = str(self.searchName.text())
        s_sname = '%' + sname + '%'
        if int(self.staff.srole) > 1:
            self.data = self.staff.showAllStaff(s_sname)
            # print(self.data)
            self.rowNum = len(self.data)
            self.columnNum = len(self.data[0])
            print(self.rowNum)
            print(self.columnNum)
            self.searchTable.setRowCount(self.rowNum)
            self.searchTable.setColumnCount(self.columnNum)
            for i, da in enumerate(self.data):
                # 字典转列表
                da = list(da.values())
                for j in range(self.columnNum):
                    self.itemContent = QTableWidgetItem(( '%s' )  % (da[j]))
                    self.searchTable.setItem(i, j, self.itemContent)
        else:
            QMessageBox().information(None, "提示", "权限不符合要求！", QMessageBox.Yes)

    def addStaff(self):
        sid = self.inputsid.text().split()
        sname = self.inputname.text().split()
        if self.inputmale.isChecked():
            ssex = '男'
        elif self.inputfemale.isChecked():
            ssex = '女'
        else:
            ssex = ''
        stime = self.inputdate.date().toPyDate()
        susername = self.inputuser.text().split()
        spwd = self.inputpwd.text().split()
        srole = self.inputrole.text().split()
        sidcard = self.inputidcard.text().split()
        sphone = self.inputphone.text().split()
        if sid == '' or ssex == '' or sname == '' or stime == '' or susername == '' or spwd == '' \
                or srole == '' or sidcard == '' or sphone == '':
            QMessageBox().information(None, "提示", "信息不能为空！", QMessageBox.Yes)
            return False
        if int(self.staff.srole) > 1:
            ret = self.staff.addStaff(sid,sname,ssex,stime,susername,spwd,srole,sidcard,sphone)
            if ret:
                QMessageBox().information(None, "提示", "添加成功！", QMessageBox.Yes)
        else:
            QMessageBox().information(None, "提示", "权限不符合要求！", QMessageBox.Yes)

    def deleteStaff(self):
        sid = self.desid.text()
        sname = self.dename.text()
        sidcard = self.deidcard.text()
        if sid == '' or sname == '' or sidcard == '':
            QMessageBox().information(None, "提示", "信息不能为空！", QMessageBox.Yes)
            return False
        if int(self.staff.srole) > 1:
            self.staff.deleteStaff(sid,sname,sidcard)
            self.data = self.staff.showAllStaff('%%')
            print(self.data)
            self.rowNum = len(self.data)
            self.columnNum = len(self.data[0])
            self.deleteTable.setRowCount(self.rowNum)
            self.deleteTable.setColumnCount(self.columnNum)
            for i, da in enumerate(self.data):
                # 字典转列表
                da = list(da.values())
                for j in range(self.columnNum):
                    self.itemContent = QTableWidgetItem(( '%s' )  % (da[j]))
                    self.deleteTable.setItem(i, j, self.itemContent)
            QMessageBox().information(None, "提示", "删除成功！", QMessageBox.Yes)
        else:
            QMessageBox().information(None, "提示", "权限不符合要求！", QMessageBox.Yes)

    def tableDel(self):
        row_selected = self.searchTable.selectedItems()
        if len(row_selected) == 0:
            return
        row = row_selected[0].text()
        self.staff.delStaff(row)
        row = row_selected[0].row()
        self.searchTable.removeRow(row)
        QMessageBox().information(None, "提示", "删除成功！", QMessageBox.Yes)

    def tableModify(self):
        row_selected = self.searchTable.selectedItems()
        if len(row_selected) == 0:
            return
        row = row_selected[0].row()
        column  = row_selected[0].column()
        value = self.modifyvalue.text()
        self.staff.modifyStaff(row,column,value)
        tvalue = QTableWidgetItem(('%s') % (value))
        self.searchTable.setItem(row,column, tvalue)
        QMessageBox().information(None, "提示", "修改成功！", QMessageBox.Yes)



