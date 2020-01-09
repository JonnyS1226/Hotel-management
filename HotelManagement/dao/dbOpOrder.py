import pymysql
from dao.dbConfig import localSourceConfig as localConfig

class Order:
    """订单信息操作类"""
    def __init__(self,config=localConfig):
        self.db = pymysql.connect(host=config['host'],port=config['port'],user=config['user'],
                                      passwd=config['passwd'],db=config['db'],charset=config['charset'],
                                      cursorclass=config['cursorclass'])
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print("Database version : %s " % data['VERSION()'])

    def findCheckin(self,type,id,rid):
        """根据条件检索订单信息"""
        if type == '个人':
            self.cursor.execute("select * from checkin_client where cid like %s and rid like %s",
                                (id,rid))
            data = self.cursor.fetchall()
            return data
        elif type == '团队':
            self.cursor.execute("select * from checkin_team where tid like %s and rid like %s",
                                (id,rid))
            data = self.cursor.fetchall()
            return data


    def findOrder(self,id,money,rid):
        """根据条件检索订单信息"""
        self.cursor.execute("select * from hotelorder where id like %s and money>=%s and rid like %s",
                            (id,money,rid))
        data = self.cursor.fetchall()
        return data

    def findBooking(self,type,id,rid):
        """根据条件检索预定信息 """
        if type == '个人':
            self.cursor.execute("select * from booking_client where cid like %s and rid like %s",
                                (id,rid))
            data = self.cursor.fetchall()
            return data
        elif type == '团队':
            self.cursor.execute("select * from booking_team where tid like %s and rid like %s",
                                (id,rid))
            data = self.cursor.fetchall()
            return data
