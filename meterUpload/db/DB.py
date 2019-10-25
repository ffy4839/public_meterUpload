import pymysql
import pandas
from configs import *

def de_for_test(a):
   a = str(a)
   a = a.replace('[','').replace(']','').replace('"','').replace("'",'').replace('\n','')
   a = a.split(' ')
   return a

def data_for_test():
    path = r'C:\Users\ffy\Desktop\商业物联网-上告数据列表.xlsx'
    rf = pandas.read_excel(path)
    res = {}
    n = 1
    while True:
        try:
            ress = rf.iloc[n].values
        except:
            break
        res[str(n)] = de_for_test(str(ress))
        n += 1
    ress = []
    for key in res.keys():
        if key != '1':
            ress.append(tuple(zip(res['1'], res[key])))
    return ress


def show_dir(name):
    print(str(name))
    for y in [i for i in dir(name) if not i.startswith('_') ]:
        print(y)

class db():
    def __init__(self, db_name):
        self.connect_db(db_name)
        self.dbSQL = dbSQL(db_name, self.conn)


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







class dbSQL():
    def __init__(self, database_name, conn):
        self.db_name = database_name
        self.conn = conn
        self.show_version()
        self.test()

    def show_version(self):
        #显示数据库版本号
        show = None
        sql = 'select version()'
        with self.conn.cursor() as cs:
            cs.execute(sql)
            show = cs.fetchone()
            self.shows(show,'version')
        return show

    def creat_datebase(self,db_name):
        #创建数据库
        sql = "create database {}".format(db_name)
        with self.conn.cursor() as cs:
            cs.execute(sql)

    def create_table(self, tabel_name, data):
        #创建表
        data_name =','.join(['{} varchar(30)'.format(TRANSFORM_Z2E[i[0]])for i in data])
        sql = 'create table {name} ({data})'.format(name=tabel_name, data=data_name)

        try:
            with self.conn.cursor() as cs:
                cs.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def drop_table(self, table_name):
        sql = 'drop table {}'.format(table_name)
        try:
            with self.conn.cursor() as cs:
                cs.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def show_databases(self):
        # 查看数据库中的所有表
        sql = 'show databases'
        with self.conn.cursor() as cs:
            cs.execute(sql)
            show = cs.fetchall()
        self.shows(show,'all databases')
        return show

    def choose_database(self,db_name):
        #选择数据库
        dbs = self.show_databases()
        for db in dbs:
            if db_name in db:
                sql = 'use {}'.format(db_name)
                with self.conn.cursor() as cs:
                    cs.execute(sql)
                return True

    def show_tables(self):
        #查看数据库中的所有表
        sql = 'show tables'
        with self.conn.cursor() as cs:
            cs.execute(sql)
            show = cs.fetchall()
        self.shows(show,'all tables')
        return show

    def insert_into_data(self,table, data):
        #插入数据
        sql = self.insert_sql(table, data)
        try:
            with self.conn.cursor() as cs:
                cs.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)



    def insert_sql(self,table ,data):
        sql_table = '{}'.format(table)
        sql_key = ','.join([TRANSFORM_Z2E[i[0]] for i in data])
        sql_value = ','.join(['"{}"'.format(i[1]) for i in data ])

        sql = '''insert into {table} ({table_name}) values({values})'''.format(
                            table=sql_table,
                            table_name=sql_key,
                            values=sql_value)

        return sql

    def select_data(self,table,):
        sql = 'select *from {}'.format(table)
        try:
            with self.conn.cursor() as cs:
                cs.execute(sql)
                res = cs.fetchall()
            return res
        except Exception as e:
            self.conn.rollback()
            print(e)

    def shows(self, data, name):
        print(str(name).ljust(18,' '), end=': ')
        for i in range(len(data)):
            if i != len(data) - 1:
                print(data[i],end=',')
            else:
                print(data[i])

    def test(self):
        res = data_for_test()
        data = res[4]
        # print(self.choose_database('testxxssss'))
        self.choose_database('xx')
        # self.show_tables()
        # # self.create_table('hello',data)
        # self.insert_into_data('hello', data)
        res = self.select_data('hello')
        print(res,type(res))
        self.conn.close()
        # self.drop_table('hello')
        # self.creat_datebase('xxtest')






if __name__ == '__main__':
    dbs = db('meterserver')
    # res = data_for_test()
    # data = res[-1]
    # sql = ':,'.join(['"{}"'.format(i[0]) for i in data])
    #
    # print(sql)

    # print(','.join(['"{}"'.format(i[1]) for i in data]))
