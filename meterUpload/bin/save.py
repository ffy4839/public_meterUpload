


class databass():
    def __init__(self):
        pass

    def write(self, data):
        pass

    def read(self, id, databaseName):
        pass
        
class mysql():
    config = {
        'host':'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'woshiFENG99',
        'db': 'meterServer',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    def __init__(self):
        self.conn = pymysql.connect(**self.config)

    def put(self, data):

            with self.conn.cursor() as cursor:
                sql = self.creat_sql(data)
                cursor.execute(sql)
                self.conn.commit()
            print('{} | 数据库保存成功，{} 数据'.format(get_time(),data['name']))

    def creat_sql(self, data):
        sql = ''
        if data['name'] == 'upload':
            save_list = ['meter_id', 'meter_time', 'upload_time', 'upload_type', 'standard_cumulant', 'working_cumulant',
                         'billing_model', 'amount_status', 'residual_amount', 'residual_cumulant', 'price', 'periodic_cumulant',
                         'consumption_amount', 'last_recharge_amount', 'meter_type', 'measurement_status', 'measurement_status_umu',
                         'valve_status', 'voltage_state', 'battery_voltage', 'pressure', 'template', 'version', 'communication',
                         'sim', 'signal_intensity']

            sql_1 = "INSERT INTO upload "
            sql_2 = ''
            sql_4 = ''
            for i in range(len(save_list)):
                sql_2 += '{},'.format(save_list[i])
                sql_4 +='"{}",'.format(data['data'][save_list[i]])
            sql_2 = '({})'.format(sql_2[:-1])
            sql_3 = " VALUES "
            sql_4 = '({})'.format(sql_4[:-1])
            sql = sql_1 + sql_2 + sql_3 + sql_4
        return sql

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    a = mysql()
    data = {
        'name':'upload',
        'data': {'amount_status': '正常',
     'battery_voltage': '5.2',
     'billing_model': '后台预付费',
     'communication': '移动',
     'consumption_amount': '42948704.23',
     'last_recharge_amount': '999.0',
     'measurement_status': '正常',
     'measurement_status_umu': '正常',
     'meter_id': '552019070302',
     'meter_time': '2019-07-30 14:23:17',
     'meter_type': '超声波表具',
     'periodic_cumulant': '9.83',
     'plaintext_length': '005D',
     'pressure': '99.84',
     'price': '5.0123',
     'residual_amount': '968.73',
     'residual_cumulant': '193.27',
     'signal_intensity': '21',
     'sim': '89860410111840125815',
     'standard_cumulant': '70.93',
     'template': '26.06',
     'upload_time': '2019-07-30 14:23:29',
     'upload_type': '按键抄表',
     'valve_status': '开阀',
     'version': '软件版本：V1.0.9 硬件版本：V1.0.0',
     'voltage_state': '正常',
     'working_cumulant': '73.78'}
    }
    a.put(data)
    a.close()





