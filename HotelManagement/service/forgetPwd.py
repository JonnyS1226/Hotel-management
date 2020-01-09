from PyQt5.QtWidgets import QMainWindow,QMessageBox
from ui.ForgetPwd import Ui_MainWindow
from dao.dbOpStaff import Staff


class fpWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(fpWindow, self).__init__(parent)
        self.setupUi(self)
        self.retLogin.clicked.connect(self.returnToLogin)
        self.commitButton.clicked.connect(self.commit)

    def returnToLogin(self):
        from service.loginOp import MyWindow
        self.Mainwindow = MyWindow()
        self.close()
        self.Mainwindow.show()

    def commit(self):
        newPwd = self.lineEdit_newpwd.text()
        sid = self.lineEdit_id.text()
        sidcard = self.lineEdit_idcard.text()
        if sid == '' or newPwd == '' or sidcard == '':
            QMessageBox().information(None, "提示", "信息不能为空！", QMessageBox.Yes)
            return False
        s = Staff()
        ret = s.forgetPasswd(newPwd, sid, sidcard)
        if ret == True:
            QMessageBox().information(None, "提示", "修改密码成功，进入登录页面！", QMessageBox.Yes)
            from service.loginOp import MyWindow
            self.Mainwindow = MyWindow()
            self.close()
            self.Mainwindow.show()
        else:
            QMessageBox().information(None, "提示", "找回密码失败！", QMessageBox.Yes)