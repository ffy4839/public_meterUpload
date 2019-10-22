import pymysql


def show_dir(name):
    print(str(name))
    for y in [i for i in dir(name) if not i.startswith('_') ]:
        print(y)

class db():
    def __init__(self, db_name):
        self.connect_db(db_name)
        self.dbSQL = dbSQL(db_name, self.conn, self.cursor)


    def connect_db(self, db_name):
        #连接数据库
        self.conn = pymysql.connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    password='woshiFENG99',
                    charset='utf8'
                    )
        # show(self.conn)
        self.cursor = self.conn.cursor()






class dbSQL():
    def __init__(self, database_name, conn, cs):
        self.db_name = database_name
        self.conn = conn
        self.cs = cs
        self.show_version()
        self.test()

    def show_version(self):
        #显示数据库版本号
        sql = 'select version()'
        self.cs.execute(sql)
        show = self.cs.fetchone()
        self.shows(show,'version')
        return show

    def creat_datebase(self,db_name):
        #创建数据库
        sql = "create database {}".format(db_name)
        self.cs.execute(sql)

    def creat_table(self, tabel_name):
        #创建表
        pass

    def show_databases(self):
        # 查看数据库中的所有表
        sql = 'show databases'
        self.cs.execute(sql)
        show = self.cs.fetchall()
        self.shows(show,'all databases')
        return show

    def choose_database(self,db_name):
        #选择数据库
        dbs = self.show_databases()
        for db in dbs:
            if db_name in db:
                sql = 'use {}'.format(db_name)
                self.cs.execute(sql)
                return True

    def show_tables(self):
        #查看数据库中的所有表
        sql = 'show tables'
        self.cs.execute(sql)
        show = self.cs.fetchall()
        self.shows(show,'all tables')
        return show

    def create_table(self, table_name, data_list):
        pass

    def inset_into_data(self, data, table):
        #插入数据
        sql = 'ss'
        pass

    def shows(self, data, name):
        print(str(name).ljust(18,' '), end=': ')
        for i in range(len(data)):
            if i != len(data) - 1:
                print(data[i],end=',')
            else:
                print(data[i])

    def test(self):
        # print(self.choose_database('testxxssss'))
        self.choose_database('testxx')
        self.show_tables()
        # self.creat_datebase('xxtest')






if __name__ == '__main__':
    dbs = db('meterserver')
    # show(pymysql.connect.)