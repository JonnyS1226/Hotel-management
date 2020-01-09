import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from ui.LoginUI import Ui_MainWindow
from service import globalValue

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.display)
        self.forgetPasswd.clicked.connect(self.forgetPwd)


    def display(self):
        username = self.lineEdit_user.text()
        password = self.lineEdit_password.text()
        global staff
        staff = globalValue._initStaff()
        role = staff.userLogin(username,password)
        # 登录成功，返回权限，1为前台,2为管理员
        if role:
            from service.mainControl import MainWindow
            self.Mainwindow = MainWindow()
            self.close()
            self.Mainwindow.show()
        else:
            QMessageBox().information(None, "提示", "账号或密码错误！", QMessageBox.Yes)


    def forgetPwd(self):
        from service.forgetPwd import fpWindow
        self.fpWindow = fpWindow()
        self.close()
        self.fpWindow.show()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWindow()
    widget.show()
    sys.exit(app.exec_())