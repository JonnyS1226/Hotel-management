# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 600)
        MainWindow.setStyleSheet("QListWidget, QListView, QTreeWidget, QTreeView,QFrame {\n"
"    outline: 0px;\n"
"}\n"
"/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/\n"
"QListWidget {\n"
"    min-width: 200px;\n"
"    max-width: 200px;\n"
"    color: white;\n"
"    background-color:#2f4050\n"
"}\n"
"#head\n"
"{\n"
"background:white;\n"
"border-radius:30px;\n"
"}\n"
"#head_2\n"
"{\n"
"background:#CCFFCC;\n"
"border:1px solid;\n"
"border-color:#CCFFCC;\n"
"border-radius:60px;\n"
"}\n"
"#Search\n"
"{\n"
"border-radius:5px;\n"
"background:#293846;\n"
"border:0.5px solid;\n"
"border-color:white;\n"
"\n"
"}\n"
"QListWidget::item\n"
"{\n"
"height:60;\n"
"background-color:#293846;\n"
"}\n"
"#frame\n"
"{\n"
"background-color:#2f4050\n"
"\n"
"}\n"
"/*被选中时的背景颜色和左边框颜色*/\n"
"QListWidget::item:selected {\n"
"    background: rgb(52, 52, 52);\n"
"    border-left: 2px solid rgb(9, 187, 7);\n"
"}\n"
"/*鼠标悬停颜色*/\n"
"HistoryPanel::item:hover {\n"
"    background: rgb(52, 52, 52);\n"
"}\n"
"/*右侧的层叠窗口的背景颜色*/\n"
"QStackedWidget {\n"
"    background: white;\n"
"}\n"
"/*模拟的页面*/\n"
"#frame > QLabel\n"
"{\n"
"color:white;\n"
"}\n"
"#frame_2\n"
"{\n"
"background-color:#CCFFCC;\n"
"}\n"
"#page_2 > QLineEdit,QDateEdit\n"
"{\n"
"border-radius:5px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color:#6699CC;\n"
"}\n"
"#page_4 > QLineEdit\n"
"{\n"
"border-radius:5px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color:#6699CC;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 200, 204, 400))
        self.listWidget.setItemAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../pictures/customer1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../pictures/customer2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 204, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.head = QtWidgets.QToolButton(self.frame)
        self.head.setGeometry(QtCore.QRect(60, 20, 60, 60))
        self.head.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../pictures/staff3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.head.setIcon(icon2)
        self.head.setIconSize(QtCore.QSize(60, 60))
        self.head.setObjectName("head")
        self.welcome = QtWidgets.QLabel(self.frame)
        self.welcome.setGeometry(QtCore.QRect(30, 90, 110, 20))
        self.welcome.setText("")
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Search = QtWidgets.QLineEdit(self.frame)
        self.Search.setGeometry(QtCore.QRect(20, 170, 145, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.Search.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(7)
        self.Search.setFont(font)
        self.Search.setStyleSheet("")
        self.Search.setObjectName("Search")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(170, 170, 21, 20))
        self.toolButton.setStyleSheet("background-color:#2f4050;\n"
"border:0px;\n"
"\n"
"border-radius:5px")
        self.toolButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../pictures/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon3)
        self.toolButton.setIconSize(QtCore.QSize(15, 15))
        self.toolButton.setObjectName("toolButton")
        self.role = QtWidgets.QLabel(self.frame)
        self.role.setGeometry(QtCore.QRect(30, 120, 110, 15))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.role.setFont(font)
        self.role.setText("")
        self.role.setAlignment(QtCore.Qt.AlignCenter)
        self.role.setObjectName("role")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 0, 611, 601))
        self.stackedWidget.setStyleSheet("background-color:#FFFFFF\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.tableClient = QtWidgets.QTableWidget(self.page_3)
        self.tableClient.setGeometry(QtCore.QRect(0, 260, 611, 339))
        self.tableClient.setStyleSheet("")
        self.tableClient.setObjectName("tableClient")
        self.tableClient.setColumnCount(7)
        self.tableClient.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(6, item)
        self.frame_2 = QtWidgets.QFrame(self.page_3)
        self.frame_2.setGeometry(QtCore.QRect(0, 30, 611, 230))
        self.frame_2.setStyleSheet("background-color:rgb(255, 249, 246)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.searchNB = QtWidgets.QToolButton(self.frame_2)
        self.searchNB.setGeometry(QtCore.QRect(250, 170, 101, 41))
        self.searchNB.setStyleSheet("background-color:rgb(255, 249, 246);\n"
"border:0px;\n"
"\n"
"border-radius:5px")
        self.searchNB.setIcon(icon3)
        self.searchNB.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.searchNB.setObjectName("searchNB")
        self.searchName = QtWidgets.QLineEdit(self.frame_2)
        self.searchName.setGeometry(QtCore.QRect(250, 80, 181, 31))
        self.searchName.setStyleSheet("border-radius:10px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color:#CCCCFF;\n"
"")
        self.searchName.setObjectName("searchName")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(100, 73, 141, 40))
        self.label_23.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(100, 125, 101, 40))
        self.label_24.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_24.setObjectName("label_24")
        self.searchTimes = QtWidgets.QLineEdit(self.frame_2)
        self.searchTimes.setGeometry(QtCore.QRect(250, 130, 181, 31))
        self.searchTimes.setStyleSheet("border-radius:10px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color:#CCCCFF;\n"
"")
        self.searchTimes.setObjectName("searchTimes")
        self.typeC = QtWidgets.QRadioButton(self.frame_2)
        self.typeC.setGeometry(QtCore.QRect(250, 30, 81, 19))
        self.typeC.setObjectName("typeC")
        self.typeT = QtWidgets.QRadioButton(self.frame_2)
        self.typeT.setGeometry(QtCore.QRect(350, 30, 115, 19))
        self.typeT.setObjectName("typeT")
        self.label_78 = QtWidgets.QLabel(self.frame_2)
        self.label_78.setGeometry(QtCore.QRect(100, 20, 101, 41))
        self.label_78.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_78.setObjectName("label_78")
        self.tableDelB = QtWidgets.QToolButton(self.frame_2)
        self.tableDelB.setGeometry(QtCore.QRect(530, 190, 101, 41))
        self.tableDelB.setStyleSheet("background-color:rgb(255, 249, 246);\n"
"border:0px;\n"
"\n"
"border-radius:5px")
        self.tableDelB.setIcon(icon3)
        self.tableDelB.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tableDelB.setObjectName("tableDelB")
        self.split_3 = QtWidgets.QFrame(self.page_3)
        self.split_3.setGeometry(QtCore.QRect(-10, 30, 600, 2))
        self.split_3.setStyleSheet("color:#CCFFCC;\n"
"border-color:#CCFFCC;\n"
"background-color:#CCFFCC")
        self.split_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.split_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.split_3.setObjectName("split_3")
        self.toolButton_2 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_2.setGeometry(QtCore.QRect(0, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("border:none")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../../pictures/search1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon4)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.split_2 = QtWidgets.QFrame(self.page_2)
        self.split_2.setGeometry(QtCore.QRect(0, 30, 600, 2))
        self.split_2.setStyleSheet("color:#CCFFCC;\n"
"border-color:#CCFFCC;\n"
"background-color:#CCFFCC")
        self.split_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.split_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.split_2.setObjectName("split_2")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(100, 270, 101, 41))
        self.label_11.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(100, 370, 101, 41))
        self.label_13.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_13.setObjectName("label_13")
        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(100, 420, 101, 41))
        self.label_16.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(100, 470, 101, 41))
        self.label_17.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_17.setObjectName("label_17")
        self.cname = QtWidgets.QLineEdit(self.page_2)
        self.cname.setGeometry(QtCore.QRect(220, 280, 221, 21))
        self.cname.setObjectName("cname")
        self.cid = QtWidgets.QLineEdit(self.page_2)
        self.cid.setGeometry(QtCore.QRect(220, 430, 221, 21))
        self.cid.setObjectName("cid")
        self.cphone = QtWidgets.QLineEdit(self.page_2)
        self.cphone.setGeometry(QtCore.QRect(220, 480, 221, 21))
        self.cphone.setObjectName("cphone")
        self.toolButton_3 = QtWidgets.QToolButton(self.page_2)
        self.toolButton_3.setGeometry(QtCore.QRect(0, 0, 111, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setStyleSheet("border:none\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../../../pictures/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon5)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.commitAdd = QtWidgets.QPushButton(self.page_2)
        self.commitAdd.setGeometry(QtCore.QRect(200, 550, 211, 31))
        self.commitAdd.setStyleSheet("#commitAdd{background:#CCFFCC;\n"
"border-radius:8px}\n"
"#commitAdd:hover\n"
"{\n"
"background:#CCFF99\n"
"}")
        self.commitAdd.setObjectName("commitAdd")
        self.cfemale = QtWidgets.QRadioButton(self.page_2)
        self.cfemale.setGeometry(QtCore.QRect(320, 380, 115, 19))
        self.cfemale.setObjectName("cfemale")
        self.cmale = QtWidgets.QRadioButton(self.page_2)
        self.cmale.setGeometry(QtCore.QRect(220, 380, 81, 19))
        self.cmale.setObjectName("cmale")
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(100, 320, 101, 41))
        self.label_12.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_12.setObjectName("label_12")
        self.cage = QtWidgets.QLineEdit(self.page_2)
        self.cage.setGeometry(QtCore.QRect(220, 330, 221, 21))
        self.cage.setObjectName("cage")
        self.line_2 = QtWidgets.QFrame(self.page_2)
        self.line_2.setGeometry(QtCore.QRect(0, 240, 611, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tid = QtWidgets.QLineEdit(self.page_2)
        self.tid.setGeometry(QtCore.QRect(230, 110, 221, 21))
        self.tid.setObjectName("tid")
        self.tphone = QtWidgets.QLineEdit(self.page_2)
        self.tphone.setGeometry(QtCore.QRect(230, 160, 221, 21))
        self.tphone.setObjectName("tphone")
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(110, 50, 101, 41))
        self.label_14.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_14.setObjectName("label_14")
        self.label_18 = QtWidgets.QLabel(self.page_2)
        self.label_18.setGeometry(QtCore.QRect(110, 150, 101, 41))
        self.label_18.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_18.setObjectName("label_18")
        self.tname = QtWidgets.QLineEdit(self.page_2)
        self.tname.setGeometry(QtCore.QRect(230, 60, 221, 21))
        self.tname.setObjectName("tname")
        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(110, 100, 101, 41))
        self.label_15.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_15.setObjectName("label_15")
        self.commitAddT = QtWidgets.QPushButton(self.page_2)
        self.commitAddT.setGeometry(QtCore.QRect(200, 200, 211, 31))
        self.commitAddT.setStyleSheet("#commitAddT{background:#CCFFCC;\n"
"border-radius:8px}\n"
"#commitAddT:hover\n"
"{\n"
"background:#CCFF99\n"
"}")
        self.commitAddT.setObjectName("commitAddT")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(0, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(0, 250, 91, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "  查询和删除客户"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "  增加客户"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "*表示需要最高权限"))
        self.Search.setPlaceholderText(_translate("MainWindow", "搜索"))
        item = self.tableClient.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableClient.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableClient.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "注册时间"))
        item = self.tableClient.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "年龄"))
        item = self.tableClient.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "身份证号"))
        item = self.tableClient.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "手机号"))
        item = self.tableClient.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "入住次数"))
        self.searchNB.setText(_translate("MainWindow", "立即检索"))
        self.searchName.setPlaceholderText(_translate("MainWindow", "搜索员工姓名"))
        self.label_23.setText(_translate("MainWindow", "客户姓名/团队名称："))
        self.label_24.setText(_translate("MainWindow", "入住次数>=："))
        self.searchTimes.setPlaceholderText(_translate("MainWindow", "入住次数"))
        self.typeC.setText(_translate("MainWindow", "个人"))
        self.typeT.setText(_translate("MainWindow", "团队"))
        self.label_78.setText(_translate("MainWindow", "对象："))
        self.tableDelB.setText(_translate("MainWindow", "删除"))
        self.toolButton_2.setText(_translate("MainWindow", "查询客户"))
        self.label_11.setText(_translate("MainWindow", "客户姓名："))
        self.label_13.setText(_translate("MainWindow", "客户性别："))
        self.label_16.setText(_translate("MainWindow", "身份证："))
        self.label_17.setText(_translate("MainWindow", "手机号："))
        self.cname.setPlaceholderText(_translate("MainWindow", "姓名"))
        self.cid.setPlaceholderText(_translate("MainWindow", "身份证"))
        self.cphone.setPlaceholderText(_translate("MainWindow", "手机号"))
        self.toolButton_3.setText(_translate("MainWindow", "增添客户"))
        self.commitAdd.setText(_translate("MainWindow", "确认录入"))
        self.cfemale.setText(_translate("MainWindow", "女"))
        self.cmale.setText(_translate("MainWindow", "男"))
        self.label_12.setText(_translate("MainWindow", "客户年龄："))
        self.cage.setPlaceholderText(_translate("MainWindow", "年龄"))
        self.tid.setPlaceholderText(_translate("MainWindow", "标识"))
        self.tphone.setPlaceholderText(_translate("MainWindow", "手机号"))
        self.label_14.setText(_translate("MainWindow", "团队名称："))
        self.label_18.setText(_translate("MainWindow", "预留手机号："))
        self.tname.setPlaceholderText(_translate("MainWindow", "名称"))
        self.label_15.setText(_translate("MainWindow", "团队标识："))
        self.commitAddT.setText(_translate("MainWindow", "确认录入"))
        self.label_9.setText(_translate("MainWindow", "增加团队："))
        self.label_10.setText(_translate("MainWindow", "增加客户："))
