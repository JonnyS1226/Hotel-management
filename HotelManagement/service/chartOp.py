import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QGridLayout
from ui.report import Ui_MainWindow
from dao.dbOpChart import Chart,Figure_Canvas
from service import globalValue
import os
from dao.dbConfig import localSourceConfig as localConfig
sys.path.append('D:\mysql\bin')

class ChartOp(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(ChartOp, self).__init__(parent)
        self.setupUi(self)
        self.staff = globalValue.get_staff()
        self.welcome.setText(self.staff.sname)
        self.role.setText('权限：'+ self.staff.srole)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listWidget_4.currentRowChanged.connect(self.stackedWidget_2.setCurrentIndex)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout2 = QGridLayout(self.groupBox_2) # 同上
        lineedit1 = self.path1
        lineedit2 = self.path2
        lineedit3 = self.path3
        self.scan.clicked.connect(lambda: self.setBrowerPath(lineedit1))
        self.scan_2.clicked.connect(lambda: self.setBrowerPath(lineedit2))
        self.scan_3.clicked.connect(lambda: self.setBrowerPath(lineedit3))
        self.tosql1.clicked.connect(self.toSQLDB)
        self.tosql2.clicked.connect(self.toSQLTable)
        self.toexcel.clicked.connect(self.toExcel)
        self.ask.clicked.connect(self.help)
        self.showfigure1.clicked.connect(self.figureOrder)
        self.showfigure2.clicked.connect(self.figureCS)

    def setBrowerPath(self,lineedit):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self,"选择导出目录","D:\pictures")
        lineedit.setText(download_path)

    def toSQLDB(self):
        """导出整个库"""
        key = localConfig['passwd']
        path = self.path1.text()
        os.system("mysqldump -uroot -p%s dbdesign > %s/dbdesign.sql" % (key,path))
        QMessageBox().information(None, "提示", "导出数据库完成！", QMessageBox.Yes)

    def toSQLTable(self):
        """导出某个表"""
        key = localConfig['passwd']
        path = self.path2.text()
        table_name = self.name1.currentText()
        if table_name == '请选择...':
            QMessageBox.information(None,'提示','必须选择一个表',QMessageBox.Yes)
            return False
        os.system("mysqldump -uroot -p%s dbdesign %s > %s/%s.sql" %(key,table_name,path,table_name))
        QMessageBox().information(None, "提示", "导出数据库表完成！", QMessageBox.Yes)

    def toExcel(self):
        """导出某个表到excel"""
        key = localConfig['passwd']
        c = Chart()
        path = self.path3.text()
        table_name = self.name2.currentText()
        if table_name == '请选择...':
            QMessageBox.information(None,'提示','必须选择一个表',QMessageBox.Yes)
            return False
        c.toExcel(path,table_name)
        QMessageBox().information(None, "提示", "导出表格完成！", QMessageBox.Yes)

    def help(self):
        QMessageBox().information(None, "提示", "client -- 客户表\nteam -- 团队表\nstaff -- 员工表\nroom -- 房间表"
                                              "\ncheckin_client -- 入住个人客户表"
                                              "\ncheckin_team -- 入住团体表\nbooking_client -- 个人预约表\n"
                                              "booking_team -- 团体预约表\nhotelorder -- 完成订单表", QMessageBox.Yes)

    def figureOrder(self):
        self.plotRevenue()
        self.plotOccupy()


    def plotRevenue(self):
        c = Chart()
        x, y = c.getRevenue()
        F = Figure_Canvas(width=6, height=2, dpi=100)
        F.axes.plot(x, y)

        F.fig.suptitle("revenue in 7 days")
        self.gridlayout.addWidget(F, 1, 0)

    def plotOccupy(self):
        F1 = Figure_Canvas(width=6, height=2, dpi=100)
        F1.fig.suptitle("occupancy rate in 7 days")
        c = Chart()
        x, y = c.getOccupy()
        F1.axes.plot(x, y)
        self.gridlayout.addWidget(F1, 2, 0)


    def figureCS(self):
        self.plotClient()
        self.plotStaff()


    def plotStaff(self):
        F1 = Figure_Canvas(width=6, height=2, dpi=100)
        F1.fig.suptitle("components of client")
        c = Chart()
        component = c.getClientStatics()
        content = ['individual', 'team']
        cols = ['r','m']
        F1.axes.pie(component,labels=content,startangle=90,shadow=True,explode=(0,0.1),colors=cols,autopct='%1.1f%%')
        self.gridlayout2.addWidget(F1, 1, 0)

    def plotClient(self):
        c = Chart()
        x, y = c.getStaffStatics()
        F = Figure_Canvas(width=6, height=2, dpi=100)
        F.axes.bar(x, y)
        F.fig.suptitle("  staff performance: the order number they address")
        self.gridlayout2.addWidget(F, 2, 0)


