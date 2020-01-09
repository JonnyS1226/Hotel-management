import pymysql
from dao.dbConfig import localSourceConfig as localConfig
from service import globalValue

class Client:
    """客户信息操作类"""
    def __init__(self,config=localConfig):
        self.db = pymysql.connect(host=config['host'],port=config['port'],user=config['user'],
                                      passwd=config['passwd'],db=config['db'],charset=config['charset'],
                                      cursorclass=config['cursorclass'])
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print("Database version : %s " % data['VERSION()'])
        self.staff = globalValue.get_staff()

    def tableDelDB(self,type,id):
        """直接表格上进行删除"""
        if type == '个人':
            try:
                self.cursor.execute("delete from client where cid=%s",(id))
                self.db.commit()
                return True
            except Exception as e:
                print(e)
                return False
        elif type == '团队':
            try:
                self.cursor.execute("delete from team where tid=%s",(id))
                self.db.commit()
                return True
            except Exception as e:
                print(e)
                return False


    def findClient(self,type,name,times):
        """直接表格上进行修改"""
        name = '%' + str(name) + '%'
        print(times)
        if type == '个人':
            self.cursor.execute("select * from client where cname like %s and accomodation_times>=%s",(name,int(times)))
            data = self.cursor.fetchall()
            return data
        elif type == '团队':
            self.cursor.execute("select * from team where tname like %s and accomodation_times>=%s",(name,int(times)))
            data = self.cursor.fetchall()
            return data

    def addClientDB(self,cname,cid,cphone,cage,csex):
        """增加客户"""
        try:
            self.cursor.execute("insert into client(cname,cid,cphone,cage,csex,register_sid,accomodation_times) values(%s,%s,%s,%s,%s,%s,%s)",
                                (cname,cid,cphone,cage,csex,self.staff.sid,0))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False


    def addTeamDB(self,tname,tid,tphone):
        """增加团体"""
        try:
            self.cursor.execute("insert into team(tname,tid,tphone,check_in_sid,accomodation_times) values(%s,%s,%s,%s,%s)",
                                (tname,tid,tphone,self.staff.sid,0))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
