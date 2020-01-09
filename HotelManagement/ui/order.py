# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        icon.addPixmap(QtGui.QPixmap("../../../../../pictures/staff5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("../../../../../pictures/staff2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../pictures/customer1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 204, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.head = QtWidgets.QToolButton(self.frame)
        self.head.setGeometry(QtCore.QRect(60, 20, 60, 60))
        self.head.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../pictures/staff3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.head.setIcon(icon3)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../../pictures/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon4)
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
        self.stackedWidget.setGeometry(QtCore.QRect(210, 0, 611, 601))
        self.stackedWidget.setStyleSheet("background-color:#FFFFFF\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.tableBooking = QtWidgets.QTableWidget(self.page_3)
        self.tableBooking.setGeometry(QtCore.QRect(-10, 260, 611, 339))
        self.tableBooking.setStyleSheet("")
        self.tableBooking.setObjectName("tableBooking")
        self.tableBooking.setColumnCount(6)
        self.tableBooking.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(5, item)
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
        self.searchNB.setIcon(icon4)
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
        self.searchRid = QtWidgets.QLineEdit(self.frame_2)
        self.searchRid.setGeometry(QtCore.QRect(250, 130, 181, 31))
        self.searchRid.setStyleSheet("border-radius:10px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color:#CCCCFF;\n"
"")
        self.searchRid.setObjectName("searchRid")
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../../../pictures/search1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon5)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(-10, 30, 611, 235))
        self.frame_3.setStyleSheet("background-color:rgb(255, 249, 246)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.searchorderB = QtWidgets.QToolButton(self.frame_3)
        self.searchorderB.setGeometry(QtCore.QRect(250, 190, 101, 41))
        self.searchorderB.setStyleSheet("background-color:rgb(255, 249, 246);\n"
"border:0px;\n"
"\n"
"border-radius:5px")
        self.searchorderB.setIcon(icon4)
        self.searchorderB.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.searchorderB.setObjectName("searchorderB")
        self.ordername = QtWidgets.QLineEdit(self.frame_3)
        self.ordername.setGeometry(QtCore.QRect(250, 50, 181, 31))
        self.ordername.setStyleSheet("border-radius:10px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color:#CCCCFF;\n"
"")
        self.ordername.setObjectName("ordername")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(100, 43, 141, 40))
        self.label_25.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_3)
        self.label_26.setGeometry(QtCore.QRect(100, 95, 101, 40))
        self.label_26.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_26.setObjectName("label_26")
        self.ordermoney = QtWidgets.QLineEdit(self.frame_3)
        self.ordermoney.setGeometry(QtCore.QRect(250, 100, 181, 31))
        self.ordermoney.setStyleSheet("border-radius:10px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color:#CCCCFF;\n"
"")
        self.ordermoney.setObjectName("ordermoney")
        self.label_29 = QtWidgets.QLabel(self.frame_3)
        self.label_29.setGeometry(QtCore.QRect(100, 140, 101, 40))
        self.label_29.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_29.setObjectName("label_29")
        self.orderrid = QtWidgets.QLineEdit(self.frame_3)
        self.orderrid.setGeometry(QtCore.QRect(250, 145, 181, 31))
        self.orderrid.setStyleSheet("border-radius:10px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color:#CCCCFF;\n"
"")
        self.orderrid.setObjectName("orderrid")
        self.toolButton_4 = QtWidgets.QToolButton(self.page_2)
        self.toolButton_4.setGeometry(QtCore.QRect(-10, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet("border:none")
        self.toolButton_4.setIcon(icon5)
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.tableOrder = QtWidgets.QTableWidget(self.page_2)
        self.tableOrder.setGeometry(QtCore.QRect(-20, 270, 611, 339))
        self.tableOrder.setStyleSheet("")
        self.tableOrder.setObjectName("tableOrder")
        self.tableOrder.setColumnCount(9)
        self.tableOrder.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableOrder.setHorizontalHeaderItem(8, item)
        self.line = QtWidgets.QFrame(self.page_2)
        self.line.setGeometry(QtCore.QRect(0, 30, 581, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.toolButton_3 = QtWidgets.QToolButton(self.page)
        self.toolButton_3.setGeometry(QtCore.QRect(-10, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setStyleSheet("border:none")
        self.toolButton_3.setIcon(icon5)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.frame_4 = QtWidgets.QFrame(self.page)
        self.frame_4.setGeometry(QtCore.QRect(-10, 30, 611, 230))
        self.frame_4.setStyleSheet("background-color:rgb(255, 249, 246)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.searchCheckinB = QtWidgets.QToolButton(self.frame_4)
        self.searchCheckinB.setGeometry(QtCore.QRect(250, 170, 101, 41))
        self.searchCheckinB.setStyleSheet("background-color:rgb(255, 249, 246);\n"
"border:0px;\n"
"\n"
"border-radius:5px")
        self.searchCheckinB.setIcon(icon4)
        self.searchCheckinB.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.searchCheckinB.setObjectName("searchCheckinB")
        self.searchName_2 = QtWidgets.QLineEdit(self.frame_4)
        self.searchName_2.setGeometry(QtCore.QRect(250, 80, 181, 31))
        self.searchName_2.setStyleSheet("border-radius:10px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color:#CCCCFF;\n"
"")
        self.searchName_2.setObjectName("searchName_2")
        self.label_27 = QtWidgets.QLabel(self.frame_4)
        self.label_27.setGeometry(QtCore.QRect(100, 73, 141, 40))
        self.label_27.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_4)
        self.label_28.setGeometry(QtCore.QRect(100, 125, 101, 40))
        self.label_28.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_28.setObjectName("label_28")
        self.searchRid_2 = QtWidgets.QLineEdit(self.frame_4)
        self.searchRid_2.setGeometry(QtCore.QRect(250, 130, 181, 31))
        self.searchRid_2.setStyleSheet("border-radius:10px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color:#CCCCFF;\n"
"")
        self.searchRid_2.setObjectName("searchRid_2")
        self.typeC_2 = QtWidgets.QRadioButton(self.frame_4)
        self.typeC_2.setGeometry(QtCore.QRect(250, 30, 81, 19))
        self.typeC_2.setObjectName("typeC_2")
        self.typeT_2 = QtWidgets.QRadioButton(self.frame_4)
        self.typeT_2.setGeometry(QtCore.QRect(350, 30, 115, 19))
        self.typeT_2.setObjectName("typeT_2")
        self.label_79 = QtWidgets.QLabel(self.frame_4)
        self.label_79.setGeometry(QtCore.QRect(100, 20, 101, 41))
        self.label_79.setStyleSheet("font: 9pt \"FontAwesome\";")
        self.label_79.setObjectName("label_79")
        self.tableCheckin = QtWidgets.QTableWidget(self.page)
        self.tableCheckin.setGeometry(QtCore.QRect(-20, 260, 611, 339))
        self.tableCheckin.setStyleSheet("")
        self.tableCheckin.setObjectName("tableCheckin")
        self.tableCheckin.setColumnCount(7)
        self.tableCheckin.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableCheckin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCheckin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCheckin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCheckin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCheckin.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCheckin.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCheckin.setHorizontalHeaderItem(6, item)
        self.stackedWidget.addWidget(self.page)
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
        item.setText(_translate("MainWindow", "  查询预定"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "  查询订单"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "   查询入住"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "*表示需要最高权限"))
        self.Search.setPlaceholderText(_translate("MainWindow", "搜索"))
        item = self.tableBooking.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "身份证"))
        item = self.tableBooking.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "房间号"))
        item = self.tableBooking.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "开始时间"))
        item = self.tableBooking.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "结束时间"))
        item = self.tableBooking.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "预定时间"))
        item = self.tableBooking.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "备注"))
        self.searchNB.setText(_translate("MainWindow", "立即检索"))
        self.searchName.setPlaceholderText(_translate("MainWindow", "搜索编号"))
        self.label_23.setText(_translate("MainWindow", "客户编号/团队编号："))
        self.label_24.setText(_translate("MainWindow", "房间号："))
        self.searchRid.setPlaceholderText(_translate("MainWindow", "搜索房间号"))
        self.typeC.setText(_translate("MainWindow", "个人"))
        self.typeT.setText(_translate("MainWindow", "团队"))
        self.label_78.setText(_translate("MainWindow", "对象："))
        self.toolButton_2.setText(_translate("MainWindow", "查询预定"))
        self.searchorderB.setText(_translate("MainWindow", "立即检索"))
        self.ordername.setPlaceholderText(_translate("MainWindow", "搜索编号"))
        self.label_25.setText(_translate("MainWindow", "客户编号/团队编号："))
        self.label_26.setText(_translate("MainWindow", "金额数>=："))
        self.ordermoney.setPlaceholderText(_translate("MainWindow", "金额"))
        self.label_29.setText(_translate("MainWindow", "房间号："))
        self.orderrid.setPlaceholderText(_translate("MainWindow", "房间号"))
        self.toolButton_4.setText(_translate("MainWindow", "查询订单"))
        item = self.tableOrder.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "用户标识"))
        item = self.tableOrder.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "用户形式"))
        item = self.tableOrder.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "开始时间"))
        item = self.tableOrder.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "结束时间"))
        item = self.tableOrder.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "房间号"))
        item = self.tableOrder.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "支付金额"))
        item = self.tableOrder.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "备注"))
        item = self.tableOrder.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "订单时间"))
        item = self.tableOrder.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "办理的员工编号"))
        self.toolButton_3.setText(_translate("MainWindow", "查询入住"))
        self.searchCheckinB.setText(_translate("MainWindow", "立即检索"))
        self.searchName_2.setPlaceholderText(_translate("MainWindow", "搜索编号"))
        self.label_27.setText(_translate("MainWindow", "客户编号/团队编号："))
        self.label_28.setText(_translate("MainWindow", "房间号："))
        self.searchRid_2.setPlaceholderText(_translate("MainWindow", "搜索房间号"))
        self.typeC_2.setText(_translate("MainWindow", "个人"))
        self.typeT_2.setText(_translate("MainWindow", "团队"))
        self.label_79.setText(_translate("MainWindow", "对象："))
        item = self.tableCheckin.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "房间号"))
        item = self.tableCheckin.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "身份证"))
        item = self.tableCheckin.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "开始时间"))
        item = self.tableCheckin.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "结束时间"))
        item = self.tableCheckin.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "总支付金额"))
        item = self.tableCheckin.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "登记记录的员工编号"))
        item = self.tableCheckin.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "备注"))
