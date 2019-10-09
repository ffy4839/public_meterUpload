from bin.protocol import protocol
from configs import *
from protocols.protocolFunctions import protocolFunction as pf
from bin.tasklist import task
from bin.save import databass


class dataProcess():
    def __init__(self,conn, c_addr):
        self.pro = protocol()
        self.process_func = process()
        self.conn = conn
        self.c_addr = c_addr


    def connection(self, ):
        recv_data = self.recvs()
        self.meterID = recv_data['frame_parse']['meterID']
        self.meterType = recv_data['frame_parse']['meterType']
        while True:
            res = self.process(recv_data)
            if res['type'] not in ('00','01','02', 'FF','ff'):
                # 继续接受上告数据
                pass
            else:
                if res['type']  in ('00','01','02'):
                    # 结束
                    if res['data']:
                        self.sends(res['data'])
                    end = res['type']
                    break
                if res['type'] == 'FF':
                    # 下发任务
                    self.sends(res['data'])
                recv_data = self.recvs()

        self.send_end_frame(end)


    def recvs(self):
        # 接收上告数据，解析上告数据
        if self.conn:
            rec = self.pro.parse(self.conn.recv(2048))
            print('dataProcess.recvs rec-->')
            pprint.pprint( rec)
            return rec

    def sends(self,  data):
        # 组织下发数据，发送下发数据
        print('dataProcess.sends data-->',)
        pprint.pprint(data)
        cc = self.pro.frame(data)
        self.conn.send(cc)

    def send_end_frame(self,result = '00'):
        end_data = {
            'meterID': self.meterID,
            'meterType': self.meterType,
            'type': 'A55505',
            'data': {
                'result': result
            }
        }
        self.sends(end_data)

    def process(self, recv_data):
        '''

        :param recv_data:
        :return: {
            'type':( 通讯结束：'00','01','02', / 发送数据：'FF'/ 等待下次上告数据'else')
            'data': None / {
                            'meterID': self.meterID,
                            'meterType': self.meterType,
                            'type': 'A55505',
                            'data': {
                            'result': result
                            }
                }
        }
        '''
        return self.process_func.run(recv_data)


class processMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__processFunc__'] = []
        for k, v in attrs.items():
            if 'process_' in k:
                attrs['__processFunc__'].append(k)
                count += 1
        attrs['__processFuncCounts__'] = count
        return type.__new__(cls, name, bases, attrs)


class process(object, metaclass=processMetaclass):
    def __init__(self):
        self.task = task()
        self.databass = databass()

    def run(self, recv_data):
        control_code = recv_data['frame_parse']['controlCode']
        data_type = recv_data['frame_parse']['dataType']

        func_name = 'process_{}{}'.format(data_type, control_code)
        if func_name in self.__processFunc__:
            res = eval('self.{}'.format(func_name))(recv_data)
            return res
        return {
            'type':'00',
            'data':None
        }

    def process_A61885(self, recv):
        self.databass.write(recv)
        meterID = recv['frame_parse']['meterID']
        name = 'request_open'
        read_data = self.databass.read(meterID, name)
        read_result = read_data['read_result']
        data = read_data['data']
        type = '00'
        return {
            'type': type,
            'data': data
        }

    def process_A61985(self, recv):
        self.databass.write(recv)
        meterID = recv['frame_parse']['meterID']
        meterType = recv['frame_parse']['meterType']
        task = self.task.get_task(meterID, meterType)
        if not task:
            data = None
            type = '00'
        else:
            data = task
            type = 'FF'
        return {
            'type': type,
            'data': data
        }

    def process_851884(self, recv):
        self.databass.write(recv)
        data = None
        type = '00'
        return {
            'type': type,
            'data': data
        }

if __name__ =='__main__':
    pass