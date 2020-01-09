from PyQt5.QtWidgets import QMainWindow
from ui.MainUI import Ui_MainWindow
from service import globalValue
import time

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        """
        传入staff全局变量
        :param parent:
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.staff = globalValue.get_staff()
        print(self.staff.sname[0])
        self.welcome.setText(self.staff.sname + ',你好。你的权限为：' + self.staff.srole + '。今天是' + time.strftime("%Y-%m-%d", time.localtime()))
        self.staffbutton.clicked.connect(self.gotoStaff)
        self.roombutton.clicked.connect(self.gotoRoom)
        self.clientbutton.clicked.connect(self.gotoClient)
        self.orderbutton.clicked.connect(self.gotoOrder)
        self.chartbutton.clicked.connect(self.gotoChart)
        self.modifyPwd.clicked.connect(self.modifyPasswd)

    def modifyPasswd(self):
        from service.modifyPwd import mpWindow
        self.mpWindow = mpWindow()
        self.close()
        self.mpWindow.show()

    def gotoChart(self):
        from service.chartOp import ChartOp
        self.ChartOp = ChartOp()
        self.ChartOp.show()

    def gotoOrder(self):
        from service.orderOp import OrderOp
        self.OrderOp = OrderOp()
        self.OrderOp.show()

    def gotoClient(self):
        from service.clientOp import ClientOp
        self.ClientOp = ClientOp()
        self.ClientOp.show()

    def gotoRoom(self):
        from service.roomOp import RoomOp
        self.RoomOp = RoomOp()
        self.RoomOp.show()

    def gotoStaff(self):
        from service.staffOp import StaffOP
        self.StaffOP = StaffOP()
        self.StaffOP.show()

