from PyQt5.QtWidgets import QMainWindow,QMessageBox
from ui.ModifyPwd import Ui_MainWindow
from dao.dbOpStaff import Staff

class mpWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mpWindow, self).__init__(parent)
        self.setupUi(self)
        self.retLogin.clicked.connect(self.returnToMain)
        self.commitButton.clicked.connect(self.commit)

    def returnToMain(self):
        from service.mainControl import MainWindow
        self.Mainwindow = MainWindow()
        self.close()
        self.Mainwindow.show()

    def commit(self):
        newPwd = self.lineEdit_newpwd.text()
        oldPwd = self.lineEdit_oldpasswd.text()
        sid = self.lineEdit_sid.text()
        if newPwd == '' or oldPwd == '' or sid == '':
            QMessageBox().information(None, "提示", "信息不能为空！", QMessageBox.Yes)
            return False
        s = Staff()
        ret = s.modifyPasswd(sid, newPwd, oldPwd)
        if ret == True:
            QMessageBox().information(None, "提示", "修改密码成功，进入登录页面！", QMessageBox.Yes)
            from service.mainControl import MainWindow
            self.tmpWindow = MainWindow()
            self.close()
            self.tmpWindow.show()
        else:
            QMessageBox().information(None, "提示", "修改密码失败！", QMessageBox.Yes)