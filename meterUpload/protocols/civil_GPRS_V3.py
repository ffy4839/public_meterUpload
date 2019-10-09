'''
民用物联网2G，V3
'''

from protocols.protocolFunctions import protocolFunction
import sys
import time
import binascii
import pprint


class parseMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__parseFunc__'] = []
        for k, v in attrs.items():
            if 'parse_' in k:
                attrs['__parseFunc__'].append(k)
                count += 1
        attrs['__parseFuncCounts__'] = count
        return type.__new__(cls, name, bases, attrs)


class frameMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__frameFunc__'] = []
        for k, v in attrs.items():
            if 'frame_' in k:
                attrs['__frameFunc__'].append(k)
                count += 1
        attrs['__frameFuncCounts__'] = count
        return type.__new__(cls, name, bases, attrs)


class parse(object, metaclass=parseMetaclass):
    def __init__(self):
        self.res_data_parse = {}

    def run(self, frame):
        data = frame.data
        func_name = 'parse_{}_{}'.format(frame.dataType, frame.controlCode)

        if func_name in self.__parseFunc__:
            self.res_data_parse = eval('self.{}'.format(func_name))(data)
            return True
        else:
            return False

    def parse_A618_85(self, data):
        #request_open, 请求开通数据包, 上行
        parsed = request_open_A619_85(data)
        return parsed.res

    def parse_A619_85(self, data):
        # open_fail,upload,开通失败，抄表数据，上行
        parsed = request_open_A619_85(data)
        return parsed.res

    def parse_8518_84(self, data):
        #recharge_8518
        parsed = recharge_8518_84(data)
        return parsed.res

    def parse_8519_84(self, data):
        #price_adjustment_8519
        parsed = price_adjustment_8519_84(data)
        return parsed.res

    def parse_8519_81(self, data):
        #read_price_list_8519_81
        parsed = read_price_list_8519_81(data)
        return parsed.res

    def parse_8520_84(self, data):
        #valve_control_8520_84
        parsed = valve_control_8520_84(data)
        return parsed.res

    def parse_8521_84(self, data):
        #valve_control_8521_84
        parsed = valve_control_8521_84(data)
        return parsed.res

    def parse_8621_84(self, data):
        #set_parameter_8621_84
        parsed = set_parameter_8621_84(data)
        return parsed.res

    def parse_8621_81(self, data):
        #read_parameter_8621_81
        parsed = read_parameter_8621_81(data)
        return parsed.res

    def parse_8626_84(self, data):
        #set_project_setting_8626_84
        parsed = set_project_setting_8626_84(data)
        return parsed.res

    def parse_8626_81(self, data):
        # read_project_setting_8626_81
        parsed = read_project_setting_8626_81(data)
        return parsed.res

    def parse_8528_81(self, data):
        #read_recharge_8528_81
        parsed = read_recharge_8528_81(data)
        return parsed.res

    def parse_8853_84(self, data):
        #set_key_8853_84
        parsed = set_keyVersion_8853_84(data)
        return parsed.res

    def parse_8853_81(self, data):
        #read_key_8853_81
        parsed = read_keyVersion_8853_81(data)
        return parsed.res

    def parse_8527_81(self, data):
        #read_logging_8527_81
        parsed = read_logging_8527_81(data)
        return parsed.res

    def parse_A520_85(self, data):
        #updata_A520_85
        parsed = updata_A520_85(data)
        return parsed.res

    def parse_A658_01(self, data):
        #read_frozen_A658_81
        parsed = read_frozen_A658_81(data)
        return parsed.res

    def parse_A659_81(self, data):
        #make_up_frozen_A659_81
        parsed = make_up_frozen_A659_81(data)
        return parsed.res

    def parse_A560_86(self, data):
        #
        pass

    def parse_8856_84(self, data):
        #
        pass

    def parse_8856_81(self, data):
        ##read_remote_upgrade_8856_81
        parsed = read_remote_upgrade_8856_81(data)
        return parsed.res


    def parse_8857_04(self, data):
        #
        pass

    def parse_8857_81(self, data):
        #read_cycle_cumulation_8857_81
        parsed = read_cycle_cumulation_8857_81(data)
        return parsed.res

    def parse_A525_84(self, data):
        #set_configuration_parameter_A525_84
        parsed = set_configuration_parameter_A525_84(data)
        return parsed.res

    def parse_A525_81(self, data):
        #read_configuration_parameter_A525_81
        parsed = read_configuration_parameter_A525_81(data)
        return parsed.res

    def parse_A526_84(self, data):
        #set_DNS_A526
        parsed = set_DNS_A526_84(data)
        return parsed.res

    def parse_A526_81(self, data):
        #read_DNS_A526_81
        parsed = read_DNS_A526_81(data)
        return parsed.res

    def parse_A555_05(self, data):
        #
        pass

    def parse_A630_04(self, data):
        #
        pass


class frame(object, metaclass=frameMetaclass):

    def run(self, data):
        '''
        {
            'meterID':meterID,
            'meterType': meterType,
            'type': 'A55505',
            'data':{
                'result': '00'
                }
            }
        :param data:
        :return:
        '''
        type = data['type']
        dataType = type[:-2]
        controlCode = type[-2:]
        data = {
            'type':type,
            'data':data['data']
        }
        func_name = 'frame_{}_{}'.format(dataType, controlCode)

        if func_name in self.__frameFunc__:
            return eval('self.{}'.format(func_name))(data)
        else:
            print('framed Error')
            return False


    def frame_A618_05(self, data):
        # request_open_A61805
        frame = request_open_A618_05(data)
        return frame.res

    def frame_A619_05(self, data):
        #
        frame = open_fail_A619_05(data)
        return frame.res

    def frame_8518_04(self, data):
        #
        frame = recharge_8518_04(data)
        return frame.res

    def frame_8519_04(self, data):
        #
        frame = price_adjustment_8519_04(data)
        return frame.res

    def frame_8519_01(self, data):
        #
        frame = price_adjustment_8519_01(data)
        return frame.res

    def frame_8520_04(self, data):
        #
        frame = valve_control_8520_04(data)
        return frame.res

    def frame_8521_04(self, data):
        #
        frame = valve_control_8521_04(data)
        return frame.res

    def frame_8621_04(self, data):
        #
        frame = set_parameter_8621_04(data)
        return frame.res

    def frame_8621_01(self, data):
        #
        frame = read_parameter_8621_01(data)
        return frame.res

    def frame_8626_04(self, data):
        #
        frame = set_project_setting_8626_04(data)
        return frame.res

    def frame_8626_01(self, data):
        #
        frame = read_project_setting_8626_01(data)
        return frame.res

    def frame_8528_01(self, data):
        #
        frame = read_recharge_8528_01(data)
        return frame.res

    def frame_8853_04(self, data):
        #
        frame = set_key_8853_04(data)
        return frame.res

    def frame_8853_01(self, data):
        #
        frame = read_key_8853_01(data)
        return frame.res

    def frame_8527_01(self, data):
        #
        frame = read_logging_8527_01(data)
        return frame.res

    def frame_A520_05(self, data):
        #
        frame = updata_A520_05(data)
        return frame.res

    def frame_A658_01(self, data):
        #
        frame = read_frozen_A658_01(data)
        return frame.res

    def frame_A659_01(self, data):
        #
        frame = make_up_frozen_A659_01(data)
        return frame.res

    def frame_A660_01(self, data):
        frame = make_frame_respond_A660_01(data)
        return frame.res

    def frame_A560_06(self, data):
        #
        frame = remote_upgrade_A560_06(data)
        return frame.res

    def frame_8856_04(self, data):
        #
        frame = set_remote_upgrade_8856_04(data)
        return frame.res

    def frame_8856_01(self, data):
        #
        frame = read_remote_upgrade_8856_01(data)
        return frame.res

    def frame_8857_04(self, data):
        #
        frame = set_cycle_cumulation_8857_04(data)
        return frame.res

    def frame_8857_01(self, data):
        #
        frame = read_cycle_cumulation_8857_01(data)
        return frame.res

    def frame_A525_04(self, data):
        #
        frame = set_configuration_parameter_A525_04(data)
        return frame.res

    def frame_A525_01(self, data):
        #
        frame = read_configuration_parameter_A525_01(data)
        return frame.res

    def frame_A526_04(self, data):
        #
        frame = set_DNS_A526_04(data)
        return frame.res

    def frame_A526_01(self, data):
        #
        frame = read_DNS_A526_01(data)
        return frame.res

    def frame_A555_05(self, data):
        #
        frame = end_frame_A555_05(data)
        return frame.res

    def frame_A630_04(self, data):
        #
        frame = reset_A630_04(data)
        return frame.res


class upload(object, metaclass=parseMetaclass):
    def __init__(self, data):
        self.data = data
        self.res = {}
        self.pf = protocolFunction()
        self.run()

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def dataLength(self):
        data = self.pf.big_Endian(self.data[0:4])
        dataLength = int(data, 16) * 2
        self.data = self.data[4:]
        if len(self.data)  != dataLength:
            self.res[sys._getframe().f_code.co_name] = 0
            return False
        self.res[sys._getframe().f_code.co_name] = str(dataLength)
        return True


class download(object, metaclass=frameMetaclass):
    def __init__(self, data):
        self.data = data
        self.res = ''
        self.pf = protocolFunction()
        self.run()

    def run(self):
        if self.check_data():
            frame = self.framed()
            length = self.length(frame)
            self.res = length + frame

    def framed(self):
        return ''

    def length(self, data):
        if data:
            l = self.pf.big_Endian(hex(len(data) // 2)[2:].rjust(4, '0'))
        else:
            l = '0000'
        return l

    def check_data(self):
        if not isinstance(self.data, dict):  # 判断数据是否为字典类型，
            return False

        if len(list(set(['type','data'] + list(self.data.keys())))) != 2:  # 判断数据key是否为‘type'和'data'，
            return False

        if not isinstance(self.data['type'], str) or not isinstance(self.data['data'], dict):  #数据value 是否为 str和dict
            return False

        types = {'A61805': 12, 'A61905': 2, '851804': 3, '851904': 16, '851901': 0, '852004': 1, '852104': 1,
                 '862104': 13, '862101': 0, '862604': 8, '862601': 0, '852801': 0, '885304': 0, '885301': 0,
                 '852701': 0, 'A52005': 9, 'A65801': 1, 'A65901': 3, 'A66001': 3, 'A56006': 6, '885604': 1,
                 '885601': 0, '885704': 1, '885701': 0, 'A52504': 3, 'A52501': 0, 'A52604': 4, 'A52601': 0,
                 'A55505': 1, 'A63004': 0}

        if self.data['type'] not in types.keys():   # panduan
            return False

        if types[self.data['type']] != len(self.data['data'].keys()):
            return False

        self.data = self.data['data']
        return True

    def check_length(self, data_type):
        if len(list(set(list(self.data.keys())+ data_type))) == len(list(self.data.keys())):
            return True


class request_open_A618_05(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        checks = [
            'operationalModel', 'rechargeAmount',
            'changeMeterStockLimit', 'meterStockLimit',
            'prepaidParametersSetting', 'priceList',
            'uploadTime', 'frozenTime',
            'openValveStatus', 'projectSetting',
            'cycleCumulation', 'reserved',
        ]
        if not self.check_length(checks):
            return ''
        res = ''
        for i in checks:
            res += eval('self.{}()'.format(i))
        return res

    def operationalModel(self):
        data = self.data['operationalModel']
        types = {
            '表具后付费':'00', '表具预付费':'01', '后台预付费':'02',
            '00': '00','01':'01', '02':'02',
        }
        result = '00'
        if data in types.keys():
            result = types[data]

        return result

    def rechargeAmount(self):
        data = self.data['rechargeAmount']
        data = int(eval(data) * 100)
        result = self.pf.big_Endian(hex(data)[2:].rjust(8,'0'))
        return result

    def changeMeterStockLimit(self):
        data = self.data['changeMeterStockLimit']
        types = {
            '更改': '00','不更改':'01',
            '00': '00','01':'01',
            '0': '00','1': '01',
        }
        result = '00'
        if data in types.keys():
            result = types[data]

        return result

    def meterStockLimit(self):
        data = self.data['meterStockLimit']
        data = int(eval(data) * 100)
        result = self.pf.big_Endian(hex(data)[2:].rjust(8, '0'))
        return result

    def prepaidParametersSetting(self):
        data = self.data['prepaidParametersSetting']
        if data['smallAmountCloseValve'] == '开启':
            smallAmountCloseValve = '01'
        else:
            smallAmountCloseValve = '00'

        smallAmountAlarmThreshold = (
            self.pf.big_Endian(hex(int(eval(data['smallAmountAlarmThreshold']) * 100))[2:].rjust(8, '0'))
        )

        if data['overdraftCloseValve'] == '开启':
            overdraftCloseValve = '01'
        else:
            overdraftCloseValve = '00'

        overdraftAlarmThreshold = (
            self.pf.big_Endian(hex(int(eval(data['overdraftAlarmThreshold']) * 100))[2:].rjust(8, '0'))
        )
        result = smallAmountCloseValve + smallAmountAlarmThreshold + overdraftCloseValve + overdraftAlarmThreshold
        return result

    def priceList(self):
        data = self.data['priceList']
        func = price_adjustment_8519_04(data)
        result = func.framed()
        return result

    def uploadTime(self):
        data = self.data['uploadTime']
        uploadTypes = {
            '每天': '00', '单月': '01', '双月': '02',
            '每月': '03', '按分': '04', '按时': '05', '按天': '09',
            '指定5时': '07', '指定5日': '08'
        }
        uploadType = '00'
        if data['uploadType'] in uploadTypes.keys():
            uploadType = uploadTypes[data['uploadType']]

        if uploadType == '08' or uploadType == '07':
            res = ''.join(data['uploadDay']['uploadDay'])
        else:
            cycle = hex(int(data['uploadDay']['cycle']))[2:].rjust(2, '0')
            uploadDay = data['uploadDay']['uploadDay']
            e = 'FF'
            res = cycle + uploadDay + e
        res = uploadType + res
        return res

    def frozenTime(self):
        data = self.data['frozenTime']
        result = data
        return result

    def openValveStatus(self):
        data = self.data['openValveStatus']
        types = {
            '强制开阀': '00', '强制关阀': '01', '退出强制': '02',
            '00': '00','01': '01', '02': '02',
            '0': '00','1': '01', '2': '02',
        }
        result = '02'
        if data in types.keys():
            result = types[data]
        return result

    def projectSetting(self):
        data = self.data['projectSetting']
        func = price_adjustment_8519_04(data)
        result = func.framed()
        return result

    def cycleCumulation(self):
        data = self.data['cycleCumulation']
        data = int(eval(data) * 100)
        result = self.pf.big_Endian(hex(data)[2:].rjust(8, '0'))
        return result

    def reserved(self):
        result = '00' * 10
        return result


class open_fail_A619_05(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        openStatus = self.openStatus()
        errorCode = self.errorCode()
        return openStatus+errorCode


    def openStatus(self):
        return 'FF'

    def errorCode(self):
        if 'errorCode' in self.data.keys():
            types = {'01': '调价序号错误', '02': '运行模式错误',
                     '03': '抄表时间错误', '04': '冻结时间错误',
                     'BB': '表示未录入系统'}
            if self.data['errorCode'] in types:
                return types[self.data['errorCode']]
        return 'BB'


class recharge_8518_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        data = self.data
        checks = ['rechargeAmount','rechargeTimes','rechargeNum']
        if not self.check_length(checks):
            return ''

        rechargeAmount = self.rechargeAmount(data['rechargeAmount'])
        rechargeTimes = self.rechargeTimes(data['rechargeTimes'])
        rechargeNum = self.rechargeNum(data['rechargeNum'])

        return rechargeAmount + rechargeTimes + rechargeNum

    def rechargeAmount(self,data):
        return self.pf.big_Endian(hex(int(eval(data)*100))[2:].rjust(8, '0'))

    def rechargeTimes(self, data):
        return self.pf.big_Endian(hex(int(data))[2:].rjust(4,'0'))

    def rechargeNum(self, data):
        return self.pf.big_Endian(hex(int(data))[2:].rjust(8,'0'))


class price_adjustment_8519_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        checks = [
            'modelType', 'ladderUpdataType',
            'ladderPriceCycle', 'ladderExecuteTime',
            'ladderPrice1', 'ladderCumulation1',
            'ladderPrice2', 'ladderCumulation2',
            'ladderPrice3', 'ladderCumulation3',
            'ladderPrice4', 'ladderCumulation4',
            'ladderPrice5', 'ladderCumulation5',
            'ladderStartDay','adjustmentPriceNum',
        ]
        if not self.check_length(checks):
            return ''
        res = ''
        for i in checks:
            res+= eval('self.{}()'.format(i))
        return res

    def modelType(self):
        data = self.data['modelType']
        print('222', data)
        if data == '不修改价格表' or data == 'AA':
            return 'AA'
        if data == '表具预付费阶梯模型' or data == '01':
            return '01'
        return 'AA'

    def ladderUpdataType(self):
        data = self.data['ladderUpdataType']
        print('222', data)
        if data == '只更新价格' or data == '00':
            return '00'
        if data == '更新价格模型' or data =='01':
            return '01'
        return '00'

    def ladderPriceCycle(self):
        data = self.data['ladderPriceCycle']
        print('222', data)
        unit_type = {
             '月': '0', '天':'1', '日':'1','0':'0','1':'1'
         }
        unit = '1'
        if data['unit'] in unit_type.keys():
            unit = unit_type[data['unit']]

        model = '00'
        model_type = {
            '不同阶梯内价格不同': '00', ' T使用相同的价格进行结算': '01',
            '00': '00', '01': '01'

        }
        if data['model'] in model_type.keys():
            model = model_type[data['model']]

        cycle_time = bin(int(data['time']))[2:].rjust(5,'0')

        return hex(int((unit + model + cycle_time), 2))[2:].rjust(2,'0')

    def ladderExecuteTime(self):
        data = self.data['ladderExecuteTime']
        try:
            if '-' in data and ':' in data:
                res = time.strftime('%y%m%d%H', time.strptime(data,'%Y-%m-%D %H:%M:%S'))
            else:
                res = time.strftime('%y%m%d%H', time.strptime(data,'%Y%m%D%H%M%S'))
        except:
            res = time.strftime('%y%m%d%H', time.localtime(time.time()))
        return res

    def price(self, data):
        if '.' in data:
            data = data.split('.')
        else:
            data = [data, '0']

        int_data,float_data = data

        res = self.pf.big_Endian(hex(int(float_data))[2:].rjust(4, '0')) + \
              self.pf.big_Endian(hex(int(int_data))[2:].rjust(4, '0'))

        return res

    def ladderPrice1(self):
        data = self.data['ladderPrice1']
        return self.price(data)

    def ladderPrice2(self):
        data = self.data['ladderPrice2']
        return self.price(data)

    def ladderPrice3(self):
        data = self.data['ladderPrice3']
        return self.price(data)

    def ladderPrice4(self):
        data = self.data['ladderPrice4']
        return self.price(data)

    def ladderPrice5(self):
        data = self.data['ladderPrice5']
        return self.price(data)

    def cycle_cumulation(self, data):
        if '.' in data: data = data.split('.')
        else: data = [data,'0']
        return self.pf.big_Endian(hex(int(data[1]))[2:].rjust(2, '0')) + \
               self.pf.big_Endian(hex(int(data[0]))[2:].rjust(6, '0'))


    def ladderCumulation1(self):
        data = self.data['ladderCumulation1']
        return self.cycle_cumulation(data)

    def ladderCumulation2(self):
        data = self.data['ladderCumulation2']
        return self.cycle_cumulation(data)

    def ladderCumulation3(self):
        data = self.data['ladderCumulation3']
        return self.cycle_cumulation(data)

    def ladderCumulation4(self):
        data = self.data['ladderCumulation4']
        return self.cycle_cumulation(data)

    def ladderCumulation5(self):
        data = self.data['ladderCumulation5']
        return self.cycle_cumulation(data)

    def ladderStartDay(self):
        data = self.data['ladderStartDay']
        year = bin(int(data['year']))[2:].rjust(7,'0')
        month = bin(int(data['month']))[2:].rjust(4,'0')
        day = bin(int(data['day']))[2:].rjust(5,'0')
        return self.pf.big_Endian(hex(int((year+month+day),2))[2:].rjust(4,'0'))

    def adjustmentPriceNum(self):
        data = self.data['adjustmentPriceNum']
        return self.pf.big_Endian(hex(int(data))[2:].rjust(8,'0'))


class price_adjustment_8519_01(download):
    def __init__(self, data):
        super().__init__(data)


class valve_control_8520_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        data = self.data
        types = {
             '强制开阀':'AA', '强制关阀':'55' ,
             '退出强制':'99', '开阀':'77', '关阀':'88'
        }

        res = '77'
        if data['valveControl'] in types.keys():
            res = types[data['valveControl']]
        return res


class valve_control_8521_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        data = self.data
        types = {
            '强制开阀': 'AA', '强制关阀': '55',
            '退出强制': '99', '开阀': '77', '关阀': '88'
        }
        res = '77'
        if data['valveControl'] in types.keys():
            res = types[data['valveControl']]
        return res


class set_parameter_8621_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        checks = [
            'uploadTimeAble', 'uploadTime',
            'frozenTimeAble', 'frozenTime',
            'stockLimitAble', 'stockLimit',
            'prepaidParametersAble', 'prepaidParameters',
            'IPportAble', 'IPport',
            'netParameterAble', 'netParameter',
            'reserved',
        ]
        if not self.check_length(checks):
            return ''
        res = ''
        for i in checks:
            res += eval('self.{}()'.format(i))
        return res

    def uploadTimeAble(self):
        data = self.data['uploadTimeAble']
        if data == '更改':
            res = '01'
        else:
            res = '00'
        return res

    def frozenTimeAble(self):
        data = self.data['frozenTimeAble']
        if data == '更改':
            res = '01'
        else:
            res = '00'
        return res

    def stockLimitAble(self):
        data = self.data['stockLimitAble']
        if data == '更改':
            res = '01'
        else:
            res = '00'
        return res

    def prepaidParametersAble(self):
        data = self.data['prepaidParametersAble']
        if data == '更改':
            res = '01'
        else:
            res = '00'
        return res

    def IPportAble(self):
        data = self.data['IPportAble']
        if data == '更改':
            res = '01'
        else:
            res = '00'
        return res

    def netParameterAble(self):
        data = self.data['netParameterAble']
        if data == '更改':
            res = '01'
        else:
            res = '00'
        return res

    def uploadTime(self):
        data = self.data['uploadTime']
        uploadTypes = {
            '每天':'00', '单月':'01', '双月':'02',
            '每月':'03', '按分':'04', '按时':'05', '按天':'09',
            '指定5时':'07', '指定5日':'08'
        }
        uploadType = '00'
        if data['uploadType'] in uploadTypes.keys():
            uploadType = uploadTypes[data['uploadType']]

        if uploadType == '08' or uploadType == '07':
            res = ''.join(data['uploadDay']['uploadDay'])
        else:
            cycle = hex(int(data['uploadDay']['cycle']))[2:].rjust(2,'0')
            uploadDay = data['uploadDay']['uploadDay']
            e = 'FF'
            res = cycle + uploadDay + e
        res = uploadType + res
        return res

    def frozenTime(self):
        data = self.data['frozenTime']
        return data

    def stockLimit(self):
        data = self.data['stockLimit']
        res = self.pf.big_Endian(hex(int(eval(data) * 100))[2:].rjust(8,'0'))
        return res

    def prepaidParameters(self):
        data = self.data['prepaidParameters']
        if data['smallAmountCloseValve'] == '开启':
            smallAmountCloseValve = '01'
        else:
            smallAmountCloseValve = '00'

        smallAmountAlarmThreshold = (
            self.pf.big_Endian(hex(int(eval(data['smallAmountAlarmThreshold']) * 100))[2:].rjust(8,'0'))
        )

        if data['overdraftCloseValve'] == '开启':
            overdraftCloseValve = '01'
        else:
            overdraftCloseValve = '00'

        overdraftAlarmThreshold = (
            self.pf.big_Endian(hex(int(eval(data['overdraftAlarmThreshold']) * 100))[2:].rjust(8,'0'))
        )
        res = smallAmountCloseValve + smallAmountAlarmThreshold + overdraftCloseValve + overdraftAlarmThreshold
        return res

    def IPport(self):
        data = self.data['IPport']
        if data['flag'] == '域名':
            flag = '20'
        else:
            flag = 'FF'

        IPport = ''
        ip = data['IPport'].split(':')[0].split('.')
        for i in ip:
            IPport += hex(int(i))[2:].rjust(2,'0')
        port = data['IPport'].split(':')[1]
        IPport += hex(int(port))[2:].rjust(4,'0')
        return flag+IPport

    def netParameter(self):
        data = self.data['netParameter']
        userName = data['userName']
        key = data['key']

        userName = binascii.hexlify(userName.encode()).decode('ASCII').upper()
        key = binascii.hexlify(key.encode()).decode('ASCII').upper()

        L_userName = hex(int(len(userName)//2))[2:].rjust(2,'0')
        L_key = hex(int(len(key)//2))[2:].rjust(2,'0')

        return L_userName + userName + L_key + key

    def reserved(self):
        return '00'*25


class read_parameter_8621_01(download):
    def __init__(self, data):
        super().__init__(data)


class set_project_setting_8626_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        checks = [
            'valveControlAbleChangeBit', 'valveControlAbleBit',
            'parameterModificationAbleBit', 'smallFlowAlarmThreshold',
            'largeFlowAlarmThreshold', 'notUseDays',
            'lossSignalDays', 'reservedFrame',
        ]
        if not self.check_length(checks):
            return ''
        res = ''
        for i in checks:
            res += eval('self.{}()'.format(i))
        return res

    def valveControlAbleChangeBit(self):
        data = self.data['valveControlAbleChangeBit']
        types = [
            '119报警关阀功能', '上电是否直接开阀', '欠压是否关阀', '小流量是否关阀',
            '超流量是否关阀', '反向走气是否关阀', '温度传感器坏是否关阀', '压力传感器坏是否关阀',
            '开阀是否需要按键', '掉电是否关阀', '闲置是否关阀', '失联是否关阀',
            '拆表是否关阀', 'Bit13', 'Bit14', 'Bit15',
        ]
        types.reverse()
        res = ''
        for i in types:
            if i in data.keys():
                res += data[i]
        res = hex(int(res, 2))[2:].rjust(2,'')
        return res

    def valveControlAbleBit(self):
        data = self.data['valveControlAbleBit']
        types = [
            '119报警关阀功能', '上电是否直接开阀', '欠压是否关阀', '小流量是否关阀',
            '超流量是否关阀', '反向走气是否关阀', '温度传感器坏是否关阀', '压力传感器坏是否关阀',
            '开阀是否需要按键', '掉电是否关阀', '闲置是否关阀', '失联是否关阀',
            '拆表是否关阀', 'Bit13', 'Bit14', 'Bit15',
        ]
        types.reverse()
        res = ''
        for i in types:
            if i in data.keys():
                res += data[i]
        res = hex(int(res, 2))[2:].rjust(2, '')
        return res

    def parameterModificationAbleBit(self):
        data = self.data['parameterModificationAbleBit']
        types = ['小流报警阈值','大流报警阈值','闲置的天数','失联的天数',
                 'Bit4','Bit5','Bit6','Bit7',]
        types.reverse()
        res = ''
        for i in types:
            if i in data.keys():
                res += data[i]
        res = hex(int(res, 2))[2:].rjust(2, '')
        return res

    def smallFlowAlarmThreshold(self):
        data = self.data['smallFlowAlarmThreshold']
        return hex(int(eval(data) * 10000))[2:].rjust(8,'')

    def largeFlowAlarmThreshold(self):
        data = self.data['largeFlowAlarmThreshold']
        return hex(int(eval(data) * 10000))[2:].rjust(8, '')

    def notUseDays(self):
        data = self.data['notUseDays']
        return hex(int(eval(data)))[2:].rjust(2, '')

    def lossSignalDays(self):
        data = self.data['lossSignalDays']
        return hex(int(eval(data)))[2:].rjust(2, '')

    def reservedFrame(self):
        return '00'*22


class read_project_setting_8626_01(download):
    def __init__(self, data):
        super().__init__(data)


class read_recharge_8528_01(download):
    def __init__(self, data):
        super().__init__(data)


class set_key_8853_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        checks = [
            'keyVersion','key'
        ]
        if not self.check_length(checks):
            return ''
        res = ''
        for i in checks:
            res += eval('self.{}()'.format(i))
        return res

    def keyVersion(self):
        data = self.data['keyVersion']
        return hex(int(eval(data)))[2:].rjust(2,'0')

    def key(self):
        data = self.data['key']
        return data


class read_key_8853_01(download):
    def __init__(self, data):
        super().__init__(data)


class read_logging_8527_01(download):
    def __init__(self, data):
        super().__init__(data)


class updata_A520_05(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        checks = [
            'cycleCumulation', 'lastAmount',
            'lastRechargeAmount', 'price',
            'lastSettleTime', 'lastRechargeTime',
            'remainingGas', 'status',
            'reserved',
        ]
        if not self.check_length(checks):
            return ''
        res = ''
        for i in checks:
            res += eval('self.{}()'.format(i))
        return res

    def cycleCumulation(self):
        data = self.data['cycleCumulation']
        return self.pf.unnegative(data,2,8)

    def lastAmount(self):
        data = self.data['lastAmount']
        return self.pf.unnegative(data,2,8)


    def lastRechargeAmount(self):
        data = self.data['lastRechargeAmount']
        return self.pf.unnegative(data, 2, 8)

    def price(self):
        data = self.data['price']
        return self.pf.unnegative(data, 4, 8)

    def lastSettleTime(self):
        data = self.data['lastSettleTime']
        try:
            res = time.strftime('%y%m%d%H%M%S', time.strptime(data,'%Y-%m-%d %H:%M:%S'))
        except:
            res = data
        return res


    def lastRechargeTime(self):
        data = self.data['lastRechargeTime']
        try:
            res = time.strftime('%y%m%d%H%M%S', time.strptime(data,'%Y-%m-%d %H:%M:%S'))
        except:
            res = data
        return res

    def remainingGas(self):
        data = self.data['remainingGas']
        return self.pf.unnegative(data, 2, 8)

    def status(self):
        data = self.data['status']
        types = [0] * 16
        types[7] = int(data['cycleCumulation'])
        types[2] = int(data['lastAmount'])
        types[1] = int(data['remainingGas'])
        types.reverse()
        return ''.join([str(i) for i in types])

    def reserved(self):
        return '00'*10


class read_frozen_A658_01(download):
    def __init__(self, data):
        super().__init__(data)


class make_up_frozen_A659_01(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        checks = [
            'type', 'startTime','overTime'
        ]
        if not self.check_length(checks):
            return ''
        res = ''
        for i in checks:
            res += eval('self.{}()'.format(i))
        return res

    def type(self):
        data = self.data['type']
        types = {
            '月':'02','月冻结':'02','日':'01','日冻结':'01','天':'01','天冻结':'01',
        }
        res = '01'
        if data in types.keys():
            res = types[data]
        return  res

    def startTime(self):
        data = self.data['startTime']
        try:
            res = time.strftime('%y%m%d', time.strptime(data,'%Y-%m-%d'))
        except:
            res = data
        return res

    def overTime(self):
        data = self.data['overTime']
        try:
            res = time.strftime('%y%m%d', time.strptime(data,'%Y-%m-%d'))
        except:
            res = data
        return res


class make_frame_respond_A660_01(make_up_frozen_A659_01):
    def __init__(self, data):
        super().__init__(data)


class remote_upgrade_A560_06(download):
    def __init__(self, data):
        super().__init__(data)


class set_remote_upgrade_8856_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        data = self.data['time']
        return self.pf.big_Endian(hex(eval(data))[2:].rjust(4,'0'))


class read_remote_upgrade_8856_01(download):
    def __init__(self, data):
        super().__init__(data)


class set_cycle_cumulation_8857_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        data = self.data['cycleCumulation']
        return self.pf.unnegative(data)


class read_cycle_cumulation_8857_01(download):
    def __init__(self, data):
        super().__init__(data)


class set_configuration_parameter_A525_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        checks = [
            'configurationParameterAble', 'parameterChangeAble','reserved'
        ]
        if not self.check_length(checks):
            return ''
        res = ''
        for i in checks:
            res += eval('self.{}()'.format(i))
        return res

    def configurationParameterAble(self):
        data = self.data['configurationParameterAble']
        types = ['0'] * 16
        types[0] = str(int(data['错峰']))
        types[1] = str(int(data['重复上告']))
        types[2] = str(int(data['结算类型']))
        types.reverse()
        res = hex(int(''.join(types), 2))[2:].rjust(4,'0')
        return res

    def parameterChangeAble(self):
        data = self.data['parameterChangeAble']
        res = ['0'] * 8
        if data == '气量式':
            res[2] = '1'
        res.reverse()
        res = hex(int(''.join(res), 2))[2:].rjust(2, '0')
        return res

    def reserved(self):
        return '00'*20


class read_configuration_parameter_A525_01(download):
    def __init__(self, data):
        super().__init__(data)


class reset_A630_04(download):
    def __init__(self, data):
        super().__init__(data)


class set_DNS_A526_04(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        data = self.data
        if data['enableFlag'] == '域名':
            flag = '20'
        else:
            flag = 'FF'

        DNS = binascii.hexlify(data['DNS'].encode()).decode('ASCII').upper()

        l = hex(int(len(DNS) // 2))[2:].rjust(2,'0')

        port = hex(int(data['DNSport']))[2:].rjust(4,'0')

        return flag + l + DNS + port


class read_DNS_A526_01(download):
    def __init__(self, data):
        super().__init__(data)


class end_frame_A555_05(download):
    def __init__(self, data):
        super().__init__(data)

    def framed(self):
        if 'result' not in self.data.keys():
            return '00'

        r = self.data['result']
        types = {'正常结束': '00', '开通无此表号': '01', '开通失败': '02'}
        if r not in types.keys():
            return '00'

        return types[r]


class request_open_A619_85(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_meterTime(self):
        data = self.data[0:12]
        result = self.pf.transfer_time(data)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_requestType(self):
        data = self.data[12:14]
        types = {
            '00': '移动流量',
            '01': '电信流量'
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_meterType(self):
        data = self.data[14:16]
        types = {
            '00':'霍尔',
            '01':'光电',
            '02':'超声波'
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_operationalModel(self):
        data = self.data[16:18]
        types = {
            '00': '表具后付费',
            '01': '表具预付费',
            '02': '后台预付费',
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result


    def parse_moduleTerminalNumber(self):
        data = self.data[18:58]
        result = binascii.unhexlify(data.replace(' ','').encode()).decode()
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_uploadType(self):
        data = self.data[58:60]
        types = {
            '01':'正常抄表','02': '按键抄表',
            '03': '受控抄表','04': '检定抄表','05': '磁攻击上告',
            '06': '阶梯开始上告','07': '欠压上告', '08': '少额上告',
            '09': '欠费上告', '0A': '透支上告', '0B': '计量异常上告',
            '0C': '阶梯起始日上告', '10': '119报警上告', '11': '上电上告',
            '12': '小流量上告', '13': '大流量上告', '14': '反向走气上告',
            '17': '闲置上告', '18': '闲置结束上告', '19': '漏气保护上告',
            '1A': '拆表上告', '1B': '开通成功上告', '21': '存储异常上告',
            '30': 'GPRS电池欠压上告', '31': '计量电池欠压上告',
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_signalStrength(self):
        data = self.data[60:62]
        result = str(int(data, 16))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_batteryVoltage(self):
        data = self.data[62:64]
        result = str(int(data, 16))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_voltageStatus(self):
        data = self.data[64:66]
        types = {
            '00': '正常',
            '01': '欠压'
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_amountStatus(self):
        data = self.data[66:68]
        types = {
            '00': '正常','01': '少额','02': '欠费','03': '透支','04': '透支结束',
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_measurementStatus(self):
        data = self.data[68:70]
        result = ''
        if int(data, 16) == 0:
            result = '正常'
        data = bin(int(data, 16))[2:].rjust(8, '0')
        type_list = ['光干扰', '数据异常', '直读模块供电低压', '器件损坏', '光电读取无回应', '周期采样流量过大', '本地读数少于上次读数', '异常']
        n = ','
        for i in range(len(data)):
            if i == 7:
                n = ''
            if data[i] == '1':
                result += type_list[i] + n
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_valveStatus(self):
        data = self.data[70:72]
        types = {
            '00':'无','01':'开阀','03':'关阀',
            '05':'异常','06':'阀门强开','07':'阀门强关'
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_workCumulation(self):
        data = self.data[72:80]
        result = str(round(self.pf.negative(self.pf.big_Endian(data)) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_standardCumulation(self):
        data = self.data[80:88]
        result = str(round(self.pf.negative(self.pf.big_Endian(data)) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_cycleCumulationelf(self):
        data = self.data[88:96]
        result = str(round(self.pf.negative(self.pf.big_Endian(data)) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_consumptionAmount(self):
        data = self.data[96:104]
        result = str(round(self.pf.negative(self.pf.big_Endian(data)) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_lastAmount(self):
        data = self.data[104:112]
        result = str(round(self.pf.negative(self.pf.big_Endian(data)) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_lastVolume(self):
        data = self.data[112:120]
        result = str(round(self.pf.negative(self.pf.big_Endian(data)) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_lastTimeRechargeAmount(self):
        data = self.data[120:128]
        result = str(round(self.pf.negative(self.pf.big_Endian(data)) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_price(self):
        data = self.data[128:136]
        result = str(round(int(self.pf.big_Endian(data), 16) * 0.0001, 4))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_temperature(self):
        data = self.data[136:144]
        result = str(round(self.pf.negative(self.pf.big_Endian(data)) * 0.0001, 4))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_pressure(self):
        data = self.data[144:152]
        result = str(round(self.pf.negative(self.pf.big_Endian(data)) * 0.0001, 4))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_metertingStatusUMU(self):
        data = self.data[152:154]
        types = {
            '00':'正常', '01':'小流量泄露', '02':'大流量泄露', '04':'卸表',
            '08':'反向计量', '10':'温度传感器损坏', '20':'压力传感器损坏', '40':'装表',
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_softwareVersion(self):
        data = self.data[154:166][2:]
        result = '软件版本：V{}.{}.{} 硬件版本：V{}.{}.{}'.format(data[1],data[2],data[3],data[5],data[6],data[7])
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_recentFrozen(self):
        data = self.data[166:]
        if len(data) == 0:
            return '无'
        result = []
        ress = {}
        n = 1
        for i in range(0, len(data), 20):
            ress['frozen_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(data[i:i+20][:12], '%y%m%d%H%M%S'))
            ress['frozen_data'] = str(round(int(self.pf.big_Endian(data[i:i + 20][12:]), 16) * 0.01, 4))
            result.append(ress)
            ress = {}
            n+=1
        self.res[sys._getframe().f_code.co_name[6:]] = result


class recharge_8518_84(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_rechargeAmount(self):
        data = self.pf.big_Endian(self.data[0:8])
        result = str(round(self.pf.negative(data) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_rechargeTimes(self):
        data = self.pf.big_Endian(self.data[8:12])
        result = str(int(data, 16))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_rechargeNum(self):
        data = self.pf.big_Endian(self.data[12:20])
        result = data
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_lastAmount(self):
        data = self.pf.big_Endian(self.data[20:28])
        result = str(round(self.pf.negative(data) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_rechargeResult(self):
        data = self.data[28:30]
        types = {'00': '失败', '01': '成功'}
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result


class price_adjustment_8519_84(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_adjustment_result(self):
        data = self.data
        types = {'00': '失败', '01':'成功'}
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_price_list_8519_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_modelType(self):
        data = self.data[0:2]
        type = {
            '01':'通用版表具预付费阶梯模型',
            'AA':'不修改价格表'
        }
        if data in type:
            result = type[data]
        else:
            result = '其他'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderUpdataType(self):
        data = self.data[2:4]
        type = {
            '00': '只更新价格',
            '01': '更新价格模型'
        }
        if data in type:
            result = type[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderPriceCycle(self):
        data = self.data[4:6]
        data = bin(int(data, 16))[2:].rjust(8,'0')
        unit = {'0':'月','1':'天'}[data[0:1]]
        model = data[1:3]
        if model == '00':
            model = '不同阶梯内价格不同'
        else:
            model = '阶梯使用相同的价格进行结算'
        t = int(data[3:], 2)
        result = '{}{};{}'.format(t,unit,model)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderExecuteTime(self):
        data = self.data[6:14]
        result = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(data,'%y%m%d%H'))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderPrice1(self):
        data = self.data[14:22]
        z = str(int(self.pf.big_Endian(data[4:]), 16))
        x = str(int(self.pf.big_Endian(data[0:4]),16))
        result = '{}.{}'.format(z,x)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderCumulation1(self):
        data = self.data[22:30]
        z = str(int(self.pf.big_Endian(data[2:]), 16))
        x = str(int(self.pf.big_Endian(data[0:2]), 16))
        result = '{}.{}'.format(z, x)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderPrice2(self):
        data = self.data[30:38]
        z = str(int(self.pf.big_Endian(data[4:]), 16))
        x = str(int(self.pf.big_Endian(data[0:4]), 16))
        result = '{}.{}'.format(z, x)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderCumulation2(self):
        data = self.data[38:46]
        z = str(int(self.pf.big_Endian(data[2:]), 16))
        x = str(int(self.pf.big_Endian(data[0:2]), 16))
        result = '{}.{}'.format(z, x)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderPrice3(self):
        data = self.data[46:54]
        z = str(int(self.pf.big_Endian(data[4:]), 16))
        x = str(int(self.pf.big_Endian(data[0:4]), 16))
        result = '{}.{}'.format(z, x)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderCumulation3(self):
        data = self.data[54:62]
        z = str(int(self.pf.big_Endian(data[2:]), 16))
        x = str(int(self.pf.big_Endian(data[0:2]), 16))
        result = '{}.{}'.format(z, x)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderPrice4(self):
        data = self.data[62:70]
        z = str(int(self.pf.big_Endian(data[4:]), 16))
        x = str(int(self.pf.big_Endian(data[0:4]), 16))
        result = '{}.{}'.format(z, x)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderCumulation4(self):
        data = self.data[70:78]
        z = str(int(self.pf.big_Endian(data[2:]), 16))
        x = str(int(self.pf.big_Endian(data[0:2]), 16))
        result = '{}.{}'.format(z, x)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderPrice5(self):
        data = self.data[78:86]
        z = str(int(self.pf.big_Endian(data[4:]), 16))
        x = str(int(self.pf.big_Endian(data[0:4]), 16))
        result = '{}.{}'.format(z, x)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderCumulation5(self):
        data = self.data[86:94]
        z = str(int(self.pf.big_Endian(data[2:]), 16))
        x = str(int(self.pf.big_Endian(data[0:2]), 16))
        result = '{}.{}'.format(z, x)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_ladderStartDay(self):
        data = self.data[94:98]
        data = bin(int(self.pf.big_Endian(data), 16))[2:].rjust(16,'0')
        year = str(int(data[0:7], 2)).rjust(2,'0')
        month = str(int(data[7:11], 2)).rjust(2,'0')
        day = str(int(data[11:], 2)).rjust(2,'0')
        result = "20{}-{}-{}".format(year, month, day)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_adjustmentPriceNum(self):
        data = self.data[98:106]
        result = str(int(self.pf.big_Endian(data), 16))
        self.res[sys._getframe().f_code.co_name[6:]] = result


class valve_control_8520_84(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_controlResult1(self):
        data = self.data
        types = {
            '00':'无','01':'开阀','03':'关阀','05':'异常','06':'阀门强开','07':'阀门强关',
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result


class valve_control_8521_84(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_valveControlCode(self):
        data = self.data[:2]
        types = {
            'AA':'强制开阀', '55':'强制关阀', '99':'退出强制', '77':'开阀', '88':'关阀',
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_controlResult2(self):
        data = self.data[2:4]
        types = {
            '00':'无','01':'开阀','03':'关阀','05':'异常','06':'阀门强开','07':'阀门强关',
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result


class set_parameter_8621_84(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_setParameterResult(self):
        data = self.data
        types = {
            '00':'成功', '01':'抄表时间错误', '02':'冻结时间错误', '03':'表存上限错误', '04':'网络参数错误',
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_parameter_8621_81(upload):
    #####################
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))
                # pprint.pprint(self.res)

    def parse_meterTime(self):
        data = self.data[0:12]
        try:
            result = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(data, '%y%m%d%H%M%S'))
        except:
            result = '{}:{}'.format('Error',data)
        self.res[sys._getframe().f_code.co_name[6:]] = result


    def parse_communicationType(self):
        data = self.data[12:14]
        types = {'00':'移动流量', '01':'电信流量', }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result


    def parse_meterMode(self):
        data = self.data[14:16]
        types = {'00':'霍尔', '01':'光电', '02':'超声波', }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_operationalMode(self):
        data = self.data[16:18]
        types = {'00':'表具后付费', '01':'表具预付费', '02':'后台预付费', }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_stockLimit(self):
        data = self.data[18:26]
        result = str(round(int(self.pf.negative(self.pf.big_Endian(data))) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_prepaidParameter(self):
        data = self.data[26:46]
        smallAmountCloseValve_dict = {
            '00':'不开启','01':'开启'
        }
        if data[0:2] in smallAmountCloseValve_dict:
            smallAmountCloseValve = smallAmountCloseValve_dict[data[0:2]]
        else:
            smallAmountCloseValve = 'Error'

        smallAmountAlarmThreshold = str(round(int(self.pf.negative(self.pf.big_Endian(data[2:10]))) * 0.01, 2))

        overdraftCloseValve_dict = {
            '00': '不开启', '01': '开启'
        }
        if data[0:2] in smallAmountCloseValve_dict:
            overdraftCloseValve = overdraftCloseValve_dict[data[0:2]]
        else:
            overdraftCloseValve = 'Error'

        overdraftAlarmThreshold = str(round(int(self.pf.negative(self.pf.big_Endian(data[12:20]))) * 0.01, 2))

        result = {
            'smallAmountCloseValve': smallAmountCloseValve,
            'smallAmountAlarmThreshold': smallAmountAlarmThreshold,
            'overdraftCloseValve': overdraftCloseValve,
            'overdraftAlarmThreshold': overdraftAlarmThreshold
        }
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_uploadTimeParameter(self):
        data = self.data[46:68]
        uploadType_data = data[0:2]
        uploadDay_data = data[2:]
        uploadDay = []
        uploadType_dict = {
            '00':'每天', '01':'单月', '02':'双月', '03':'每月', '04':'按分',
            '05':'按时', '07':'指定5时', '08':'指定5日', '09':'按天', }
        if uploadType_data in uploadType_dict.keys():
            uploadType = uploadType_dict[uploadType_data]
        else:
            uploadType = 'Error'
        if uploadType_data in ['00','01','02','03','04','05','09','07','08']:
            if uploadType_data == '07' or uploadType_data == '08':
                for i in range(0,len(uploadDay_data), 4):
                    uploadDay.append(uploadDay_data[i:i+4])
            else:

                cycle = str(int(uploadDay_data[0:2], 16))
                upload = uploadDay_data[2:8]
                upload = "{}日{}时{}分".format(upload[0:2],upload[2:4],upload[4:])
                uploadDay.append("{},{}".format(cycle,upload))
            uploadDay = ','.join(uploadDay)
        else:
            uploadDay = 'Error'

        result = {
            'uploadType': uploadType,
            'uploadDay': uploadDay
        }
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_monthFrozenParameter(self):
        data = self.data[68:74]
        result = '{}日{}时{}分'.format(data[0:2], data[2:4], data[4:6])
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_netParameter(self):
        data = self.data[74:-112]
        lengthUserName = int(data[0:2], 16) * 2
        userName = binascii.unhexlify(data[2:2+lengthUserName].encode('ASCII')).decode()
        lengthKey = int(data[2+lengthUserName:4+lengthUserName]) *2
        key = binascii.unhexlify(data[4+lengthUserName:2+lengthKey].encode('ASCII'))
        result = {
            'userName':userName,
            'key':key
        }
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_IPport(self):
        data = self.data[-112:-98]
        if data[0:2] == '20':
            model = '域名'
        else:
            model = 'IP地址'
        ip = [str(int(data[2:][:8][i:i+2], 16)) for i in range(0,len(data[2:][:8]), 2)]
        port = str(int(data[2:][2:], 16))
        ip = '.'.join(ip)
        result = '{}:{},{}'.format(model,ip,port)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_moduleTerminalNumber(self):
        data = self.data[-98:-58]
        result = binascii.unhexlify(data.encode('ASCII')).decode()
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_softwareVersion(self):
        data = self.data[-58:-46]

        softVersion = data[2:6]
        hardVersion = data[6:10]

        result = '软件版本：V{}.{}.{} 硬件版本：V{}.{}.{}'.format(int(softVersion[0:2]),int(softVersion[2]),int(softVersion[3]),
                                                        int(hardVersion[0:2]),int(hardVersion[2]),int(hardVersion[3]),)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_reservedFrame(self):
        result = self.data[-46:]
        self.res[sys._getframe().f_code.co_name[6:]] = result


class set_project_setting_8626_84(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_reault(self):
        data =self.data
        if data == '00':
            result = '失败'
        else:
            result = '成功'
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_project_setting_8626_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_valveControlAbleBit(self):
        data =self.data[0:4]
        data = bin(int(self.pf.big_Endian(data), 16))[2:].rjust(16,'0')
        data_list = [
        '119报警关阀功能','上电是否直接开阀','欠压是否关阀','小流量是否关阀',
        '超流量是否关阀','反向走气是否关阀','温度传感器坏是否关阀','压力传感器坏是否关阀',
        '开阀是否需要按键','掉电是否关阀','闲置是否关阀','失联是否关阀',
        '拆表是否关阀','保留','保留','保留',
        ]
        data_list.reverse()
        result = {}
        for i in range(len(data_list)):
            result[data_list[i]] = data[i]
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_smallFlowAlarmThreshold(self):
        data = self.data[4:12]
        result = str(round(int(self.pf.negative(self.pf.big_Endian(data))) * 0.0001, 4))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_largeFlowAlarmThreshold(self):
        data = self.data[12:20]
        result = str(round(int(self.pf.negative(self.pf.big_Endian(data))) * 0.0001, 4))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_notUseDays(self):
        data = self.data[20:22]
        result = str(int(data, 16))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_lossSignalDays(self):
        data = self.data[22:24]
        result = str(int(data, 16))
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_reservedFrame(self):
        result = self.data[24:]
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_recharge_8528_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_recharge(self):
        data = self.data
        result = {}

        if len(data) == int(self.res['dataLength']):
            if len(data) % 26 == 0:
                for i in range(0, len(data), 26):
                    result['recharge{}'.format(str(int(i//26)+1))] = self.recharge(data[i:i+26])
        else:
            print(len(data))
        self.res[sys._getframe().f_code.co_name[6:]] = result


    def recharge(self, data):
        rechargeTime = data[0:12]
        rechargeType = data[12:14]
        rechargeTimes = data[14:18]
        rachargeAmount = data[18:]
        print(rechargeTime)
        try:
            rechargeTime = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(rechargeTime, '%y%m%d%H%M%S'))
        except:
            pass

        rechargeType_dict = {
                    '00': '本地充值',
                    '01': '远程充值'
                }
        if rechargeType in rechargeType_dict.keys():
            rechargeType = rechargeType_dict[rechargeType]
        else:
            rechargeType = 'Error'

        rechargeTimes = str(int(self.pf.big_Endian(rechargeTimes), 16))

        rachargeAmount = str(round(int(self.pf.negative(self.pf.big_Endian(rachargeAmount))) * 0.01, 2))
        result = {
            'rechargeTime': rechargeTime,
            'rechargeType': rechargeType,
            'rechargeTimes': rechargeTimes,
            'rachargeAmount': rachargeAmount
        }
        return result


class set_keyVersion_8853_84(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_result(self):
        data = self.data
        types = {
            '01':'成功','00':'失败'
        }
        if data in types.items():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_keyVersion_8853_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_keyVersion(self):
        data = self.data
        result = str(int(data, 16))
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_logging_8527_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_log(self):
        data = self.data
        L = int(self.res['dataLength'])
        result = []
        if L % 16 == 0:
            for i in range(0, L, 16):
                result.append(self.readLog(data[i:i+16]))

        else:
            result.append(data)
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def readLog(self, data):
        logTime = data[0:12]
        try:
            logTime = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(logTime, '%y%m%d%H%M%S'))
        except:
            pass

        types = {
            '01': '计量状态', '02': '电源控制', '03': 'GPRS连接', '04': '阀门控制',
            '05': '修改参数', '06': '调价', '07': '清除', '08': '特殊指令', 'CB': '超声波状态',
        }

        status_types = {
            '01': self.log_type_one,
            '02': self.log_type_two,
            '03': self.log_type_three,
            '04': self.log_type_four,
            '05': self.log_type_five,
            '06': self.log_type_six,
            '07': self.log_type_seven,
            '08': self.log_type_eight,
            'CB': self.log_type_CB,
        }
        if data[12:14] in types.keys():
            logType = types[data[12:14]]
            typesss = data[12:14]
            if typesss in status_types.keys():
                logStatus = status_types[typesss](data[14:16])
            else:
                logStatus = 'Error'
        else:
            logType = 'Error'
            logStatus = 'Error'
        return {'logTime': logTime,
                'logType': logType,
                'logStatus': logStatus}

    def log_type_one(self, data):
        data = bin(int(data, 16))[2:].rjust(8, '0')
        types = ['小流量泄露', '大流量泄露', '卸表报警', '反向计量',
                 '温度传感器损坏', '压力传感器损坏', '计量异常', '预留Bit7', ]
        types.reverse()
        result = []
        for i in range(len(data)):
            if data[i] == '1':
                result.append(types[i])
        result = ','.join(result)
        return result

    def log_type_two(self, logTpye02data):
        types = {
            '01': '复位上电', '02': '待机上电', '03': '欠压', '04': '低压', '05': '掉电',
        }
        if logTpye02data in types.keys():
            result = types[logTpye02data]
        else:
            result = 'Error'
        return result

    def log_type_three(self, data):
        types = {
            '01': '开机失败', '02': '信号差', '03': '连接失败', '04': 'SIM卡异常', '05': '预留05',
            '06': '上告失败', '07': '信号搜寻失败', '08': '网络注册失败', '09': '网络附着时间长',
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        return result

    def log_type_four(self, data):
        types = {
            '01': '计量异常关阀', '02': '欠压关阀', '03': '低压关阀', '04': '掉电关阀', '05': '少额关阀',
            '06': '欠费关阀', '07': '透支关阀', '08': '强制关阀', '09': '退出强制', '0A': '小流关阀',
            '0B': '大流关阀', '0C': '反向关阀', '0D': '底码异常关阀（超声波）', '0E': '强制开阀', '0F': '开阀',
            '10': '关阀', '11': '漏气保护', '12': '闲置关阀', '13': '过流保护', '14': '失联关阀',
            '15': '拆表关阀', '16': '119报警'
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        return result

    def log_type_five(self, data):
        data = bin(int(data, 16))[2:].rjust(8, '0')
        types = ['更改抄表日期', '更改冻结日期', '更改预存上限', '更改预付费参数',
                 '更改IP', '更改APN', '更改唤醒周期时间', '更改备用电池的上告时间', ]

        types.reverse()
        result = []
        for i in range(len(data)):
            if data[i] == '1':
                result.append(types[i])
        result = ','.join(result)
        return result

    def log_type_six(self, data):
        if data == '01':
            result = '调价'
        else:
            result = 'Error'
        return result

    def log_type_seven(self, data):
        if data == '01':
            result = '插清除卡'
        else:
            result = 'Error'
        return result

    def log_type_eight(self, data):
        if data == '01':
            result = '远程恢复出厂设置'
        else:
            result = 'Error'
        return result

    def log_type_CB(self, data):
        types = {
            '01': '更换电池', '02': '欠压', '03': '大流量报警产生', '04': '大流量报警撤销',
            '05': '小流量泄露预警产生', '06': '小流量泄露警报撤销', '07': '拆表', '08': '重新装表',
            '09': '消除拆表警报', '10': '温度传感器故障产生', '11': '压力传感器故障产生',
            '12': '温度传感器恢复', '13': '压力传感器恢复', '14': '反向计量', '15': '反向计量撤销',
            '16': '计量故障', '17': '计量故障恢复', '30': '装表事件记录', '31': '拆表事件记录',
            '32': '取消拆表报警'
        }
        if data in types.keys():
            result = types[data]
        else:
            result = 'Error'
        return result


class updata_A520_85(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_result(self):
        meterIDs = []
        meterNum = int(self.data[0:2], 16) * 2
        if len(self.data[2:]) == meterNum:
            for i in range(0, meterNum, 12):
                meterIDs.append(self.pf.big_Endian(self.data[2:][i:i+2]))
        result = {'meterNum': meterNum,
                  'meterIDs': meterIDs}
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_frozen_A658_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_frozenData(self):
        result = []
        data = self.data
        L = self.data['dataLength']
        if L % 10 == 0:
            for i in range(0,L,10):
                d = data[i:i+10]
                frozenTime = d[0:12]
                try:
                    frozenTime = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(frozenTime,'%y%m%d%H%M%S'))
                except:
                    pass
                frozenData = str(round(self.pf.negative(self.pf.big_Endian(d[12:])) * 0.01, 2))
                result.append({
                    'frozenTime': frozenTime,
                    'frozenData': frozenData
                })
        else:
            result.append({
                    'frozenTime': 'Error',
                    'frozenData': 'Error'
                })
        self.res[sys._getframe().f_code.co_name[6:]] = result


class make_up_frozen_A659_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_frozenData(self):
        result = []
        data = self.data
        L = self.data['dataLength']
        if L % 10 == 0:
            for i in range(0,L,10):
                d = data[i:i+10]
                frozenTime = d[0:12]
                try:
                    frozenTime = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(frozenTime,'%y%m%d%H%M%S'))
                except:
                    pass
                frozenData = str(round(self.pf.negative(self.pf.big_Endian(d[12:])) * 0.01, 2))
                result.append({
                    'frozenTime': frozenTime,
                    'frozenData': frozenData
                })
        else:
            result.append({
                    'frozenTime': 'Error',
                    'frozenData': 'Error'
                })
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_remote_upgrade_8856_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_cycleTime(self):
        data = self.data
        hour = str(int(data[0:2], 16))
        min = str(int(data[2:4], 16))
        result = '{}时{}分'.format(hour,min)
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_cycle_cumulation_8857_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_cycleCumulation(self):
        data = self.data
        result = str(round(self.pf.negative(self.pf.big_Endian(data)) * 0.01, 2))
        self.res[sys._getframe().f_code.co_name[6:]] = result


class set_configuration_parameter_A525_84(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_result(self):
        data = self.data
        types = {
            '00': '失败',
            '01':'成功'
        }
        if data in types.items():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_configuration_parameter_A525_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_parameterEnableBit(self):
        data = self.data[0:4]
        resultOk = []
        resultErr = []
        data = bin(int(data, 16))[2:].rjust(16,'0')
        types = ['错峰', '重复上告', 'Bit2', 'Bit3',
                 'Bit4', 'Bit5', 'Bit6', 'Bit7',
                 'Bit8', 'Bit9', 'Bit10', 'Bit11',
                 'Bit12', 'Bit13', 'Bit14', 'Bit15']
        types.reverse()
        for i in range(len(data)):
            if data[i] == '1' and 'Bit' not in types[i]:
                resultOk.append(types[i])
            elif data[i] == '0' and 'Bit' not in types[i]:
                resultErr.append(types[i])
        resultOk = '开启;'.join(resultOk)
        resultErr = '不开启，'.join(resultErr)
        result = resultOk + resultErr
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_parameterModifyEnableBit(self):
        data = self.data[4:6]
        data = bin(int(data, 16))[2:].rjust(8,'0')
        types = ['Bit0', 'Bit1', '结算方式', 'Bit3', 'Bit4', 'Bit5', 'Bit6', 'Bit7']
        for i in range(len(data)):
            if 'Bit' not in types[i]:
                if data[i] == '0':
                    result = '金额式'
                else:
                    result = '气量式'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_reserved(self):
        result = self.data[6:]
        self.res[sys._getframe().f_code.co_name[6:]] = result


class set_DNS_A526_84(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_setDNSresult(self):
        data = self.data
        types = {
            '00':'失败', '01':'成功'
        }
        if data in types.items():
            result = types[data]
        else:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result


class read_DNS_A526_81(upload):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        if self.dataLength():
            for i in range(self.__parseFuncCounts__):
                eval('self.{}()'.format(self.__parseFunc__[i]))

    def parse_enableFlag(self):
        data = self.data[0:2]
        if data == '20':
            result = '域名'
        else:
            result = 'IP'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_DNSlength(self):
        data = self.data[2:4]
        result = str(int(data, 16)) * 2
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_DNS(self):
        data = self.data[4:-4]
        try:
            result = binascii.unhexlify(data.encode('ASCII')).decode()
        except:
            result = 'Error'
        self.res[sys._getframe().f_code.co_name[6:]] = result

    def parse_DNSport(self):
        data = self.data[-4:]
        result = str(int(data, 16))
        self.res[sys._getframe().f_code.co_name[6:]] = result
