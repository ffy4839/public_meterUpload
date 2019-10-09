from configs import *
from protocols import civil_GPRS_V3
from protocols.protocolFunctions import protocolFunction

class protocol():
    '''协议解析和组帧'''
    def __init__(self,):
        self.pf = protocolFunction()
        self.parse_frame = parsed_frame_public(self.pf)
        self.frame_frame = framed_frame_public(self.pf)
        self.framed_frame_public = framed_frame_public(self.pf)
        self.framed_frame_data = framed_frame_data(self.pf)

    def parse(self, data):
        """
        :param data: (b"h\x02\x03\x07\x19 Uh\x85\x8b\x00\x19\x07)\x16&%\x0b\x19\xa6\x00\x00\xd6H\xe3\x81\xbb(R\xc3n\
                        xfb\xc1A\xb5\xbc\x98\xf0+\xa9\x8a\xe3\xfa\xee#y^\x8a[JO\x8cS\xb1\xa8)y?FR\xd2\xd6[\x89:\xa9\
                        x85AS>\x17\xf5[;Q\x0b`\xc1\xaa\x89\xf6\xc15\xd4o@\xf0\xa4\xdb\xe4\x06\xcd\xb1\xff2\x8a\x81'\
                        xe5a\x05O7\x1a\xac\xea\x82\xf7w\xf1\xf0\xc5\xd7N\xf9\x94\x8a\x1e\x7f\x91.\xdb\xb2\x95\xe3\xcb\
                        x93\x01 \xae\x9f\x7fa*g\x10\xfe\xbaJ\x0bg\x88\xc3n\x80\xaa\xce\x83u\xaf\xac\x16")
        :return: {
            'frame_parse': parseFrame,
            'data_parse': parseData
        }
        """
        if self.parse_frame.run(data) == False:
            print(self.parse_frame.Err)
            return False
        result_parse_frame = self.parse_frame.parse_frame

        self.parse_data = parsed_frame_data(self.pf, self.parse_frame)
        if not self.parse_data.run():
            print(self.parse_data.Err)
            return False
        result_parse_data = self.parse_data.parse_data

        self.frame_parse = self.parse_frame.parse_frame
        self.data_parse = self.parse_data.parse_data
        self.frames = self.parse_frame
        self.datas = self.parse_data

        resParsed = {
            'frame_parse': result_parse_frame,
            'data_parse': result_parse_data,
            'frame': self.parse_frame,
            'data': self.parse_data
        }
        return resParsed
        # self.parse_frame = self.parse_frame.parse_frame
        # pprint.pprint(self.parse_frame)

    def frame(self, data):
        '''

        :param data: {
            'meterID':meterID,
            'meterType': meterType,
            'type': 'A55505',
            'data':{
                'result': '00'
                }
            }
        :return:
        '''
        framed_data = self.framed_frame_data.run(data)
        data = self.framed_frame_public.run(data, framed_data)
        res = self.pf.h2b(data)
        return res


class parsed_frame_public():
    '''
    解析协议公共部分
    '''
    def __init__(self, func):
        self.func = func
        self.init_setting()
        self.parse_frame = None
        self.Err = 'no err'

    def run(self, data):
        data = self.func.b2h(data)

        self.uploadFrame = data
        if not self.check(data):

            self.Err = 'check err'
            return False

        self.meterID = self.func.big_Endian(data[2:14])
        self.controlCode = data[16:18]
        self.length = self.func.big_Endian(data[18:22])
        self.sysTime = self.func.transfer_time(data[22:34])
        self.meterType = data[34:36]
        self.dataType = self.func.big_Endian(data[36:40])
        self.seq = data[40:42]
        self.keyVersion = data[42:44]
        if self.keyVersion not in KEY.keys():
            print(data)
            self.Err = 'key err'
            return False

        self.data = self.func.AES_decrypt(data[44:-4], key=KEY[self.keyVersion])
        print(self.data)
        self.parse_frame = {
            'meterID': self.meterID,
            'controlCode': self.controlCode,
            'length': self.length,
            'sysTime': self.sysTime,
            'meterType': self.meterType,
            'dataType': self.dataType,
            'seq': self.seq,
            'keyVersion': self.keyVersion,
            'data': self.data,
            'checkSum': self.checkSum,
            'uploadFrame': self.uploadFrame,
        }
        return True

    def check(self, data):
        data_check = data[-4:-2]
        s_check = self.func.checkSum(data[:-4])
        if data_check == s_check:
            self.checkSum = data_check
            return True
        else:
            self.parse_frame['checkSum'] = False

    def init_setting(self):
        self.meterID = ''
        self.controlCode = ''
        self.length = ''
        self.sysTime = ''
        self.meterType = ''
        self.dataType = ''
        self.seq = ''
        self.keyVersion = ''
        self.data = ''
        self.checkSum = ''
        self.uploadFrame = ''

class parsed_frame_data():
    '''
    解析协议数据内容部分
    '''
    def __init__(self, func, frame):
        self.func = func
        self.pframe = frame
        self.Err = 'data no err'
        self.choose(frame.meterType)
        self.parse_data = {}

    def run(self):
        res = self.pro.run(self.pframe)
        self.parse_data = self.pro.res_data_parse
        # print(res)
        return res

    def choose(self, type):
        self.pro = civil_GPRS_V3.parse()


class framed_frame_data():
    def __init__(self, func):
        self.func = func
        # self.pro = civil_GPRS_V3.frame()

    def run(self, data):
        self.choose(data)
        res = self.pro.run(data)
        print('framed_frame_data.run',res)
        res = self.func.AES_encrypt(res)
        return res

    def choose(self, type):
        type = type['meterType']
        self.pro = civil_GPRS_V3.frame()

class framed_frame_public():
    def __init__(self, func):
        self.pf = func

    def run(self, data, dataFramed):
        startFrame = '68'
        endFrame = '16'
        meterID = self.pf.big_Endian(data['meterID'])

        type = self.controlCode_dataType(data)
        controlCode = type[-1]
        dataType = type[0]
        sysTime = timeNow('%y%m%d%H%M%S')
        meterType = data['meterType']
        seq = '00'
        keyVersion = '00'

        if not dataFramed:
            dataFramed = ''
        dataField = (sysTime + meterType + dataType +
                     seq + keyVersion + dataFramed).replace(' ','').upper()
        length = self.pf.big_Endian(hex(int(len(dataField) // 2))[2:].rjust(4,'0'))

        uncheck_frame = (startFrame + meterID + startFrame +
                 controlCode + length + dataField
                 ).replace(' ','').upper()
        check = self.pf.checkSum(uncheck_frame)

        frame = uncheck_frame + check + endFrame
        return frame


    def controlCode_dataType(self, data):
        type = data['type']
        dataType = type[:-2]
        controlCode = type[-2:]
        dataType = self.pf.big_Endian(dataType)
        return (dataType, controlCode)


if __name__ == '__main__':
    test_data = '6811223344556668044B001908281011260B198500003CC12EBAE0E91818A56A21758C42BD82D98B9B6BC4E47305CC97E1C0\
8550DC050591FC7C87EDEBB7BAD9EC1A47BE81A555FDD49DA472E698B90B9D1E946EF59FE516'



    pro = protocol()

    test_data = pro.pf.h2b(test_data)
    pprint.pprint(pro.parse(test_data))

