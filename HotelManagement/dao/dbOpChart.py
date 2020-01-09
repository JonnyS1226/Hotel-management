import pymysql
from dao.dbConfig import localSourceConfig as localConfig
import xlwt
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import datetime


class Chart:
    def __init__(self,config=localConfig):
        self.db = pymysql.connect(host=config['host'], port=config['port'], user=config['user'],
                                  passwd=config['passwd'], db=config['db'], charset=config['charset'],
                                  cursorclass=config['cursorclass'])
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print("Database version : %s " % data['VERSION()'])


    def toExcel(self,path, table_name):
        """
        导出到excel表
        """
        sql = "select * from " + table_name
        self.cursor.execute(sql)
        path = str(path)
        fields = [field[0] for field in self.cursor.description]
        all_data = self.cursor.fetchall()
        # 写入excel
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1')
        for col, field in enumerate(fields):
            sheet.write(0, col, field)
        row = 1
        for i in range(len(all_data)):
            data = all_data[i].values()
            for col, field in enumerate(data):
                sheet.write(row, col, field)
            row += 1
        book.save(path+"/%s.xls" % table_name)

    def getRevenue(self):
        """
        获取营业额
        """
        list_revenue = []
        list_date = []
        for i in range(7):
            data = ()
            sum = 0
            delta = datetime.timedelta(days=i)
            date = datetime.date.today()
            date_selected = date - delta
            str_date = str(date_selected)
            list_date.append(str_date[5:])
            self.cursor.execute("select money from hotelorder where end_time=%s",(date_selected))
            data = self.cursor.fetchall()
            if data != ():
                for i in range(len(data)):
                    sum = sum + int(data[i]['money'])
            list_revenue.append(sum)
        print(list_revenue)
        print(list_date)
        list_date.reverse()
        return list_date, list_revenue

    def getOccupy(self):
        """
        获取入住率/出租率
        """
        list_occupy = []
        list_date = []
        self.cursor.execute("select count(*) from room")
        totalRoomCount = self.cursor.fetchall()[0]['count(*)']
        print(totalRoomCount)
        for i in range(7):
            data = ()
            occupyRate = 0.0
            delta = datetime.timedelta(days=i)
            date = datetime.date.today()
            date_selected = date - delta
            str_date = str(date_selected)
            list_date.append(str_date[5:])
            self.cursor.execute("select distinct rid from hotelorder where end_time>=%s and start_time<=%s",
                                (date_selected,date_selected))
            data = self.cursor.fetchall()
            print(data)
            if data != ():
                occupyRate = float(len(data) / totalRoomCount)
            list_occupy.append(occupyRate)
        print(list_occupy)
        list_date.reverse()
        return list_date, list_occupy



    def getClientStatics(self):
        """
        获取客户相关数据
        """
        list_clientStatics = []
        self.cursor.execute("select * from hotelorder where ordertype='个人'")
        num_client = len(self.cursor.fetchall())
        self.cursor.execute("select distinct id from hotelorder where ordertype='团队'")
        num_team = len(self.cursor.fetchall())
        list_ret = []
        list_ret.append(num_client)
        list_ret.append(num_team)
        return list_ret



    def getStaffStatics(self):
        """
        获取员工相关数据
        """
        self.cursor.execute("select register_sid,count(*) from hotelorder group by register_sid")
        data = self.cursor.fetchall()
        list_clientNum = []
        list_clientSta = []
        for i in range(len(data)):
            list_clientNum.append(data[i]['register_sid'])
            list_clientSta.append(data[i]['count(*)'])
        print(list_clientNum)
        print(list_clientSta)
        return list_clientNum, list_clientSta


# 继承FigureCanvas类
# 这样既可以使用matplotlib，也可以通过控件展示在gui上
class Figure_Canvas(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 在父类中激活Figure窗口
        super(Figure_Canvas, self).__init__(self.fig)
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号
        self.axes = self.fig.add_subplot(111)



