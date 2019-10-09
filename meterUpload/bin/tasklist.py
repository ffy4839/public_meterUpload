





class task():
    def __init__(self):
        pass

    def get_task(self, meterID, meterType):
        '''
        :param meterID:
        :return:
         data = {
            'meterID':meterID,
            'meterType': meterType,
            'type': 'dataType + controlCode',
            'data':{
                }
            }

        '''
        data = {
            'meterID': meterID,
            'meterType': meterType,
            'type': '851904',
            # 'data': None
            'data': {
                'modelType':'表具预付费阶梯模型',
                'ladderUpdataType': '更新价格模型',
                'ladderPriceCycle':{
                    'unit':'月','model':'00','time':'12'
                },
                'ladderExecuteTime':'19082301',
                'ladderPrice1':'1.2345',
                'ladderCumulation1':'5',
                'ladderPrice2': '2.2345',
                'ladderCumulation2': '15',
                'ladderPrice3': '3.2345',
                'ladderCumulation3': '25',
                'ladderPrice4': '4.2345',
                'ladderCumulation4': '35',
                'ladderPrice5': '5.2345',
                'ladderCumulation5': '9999999',
                'ladderStartDay':{
                    'year':'19',
                    'month':'08',
                    'day':'01'
                },
                'adjustmentPriceNum':'60',
            }

        }
        return data  #无则返回None

    def put_task(self, data):
        '''

        :param data: data = {
            'meterID': 'xxxxxxxxxx',
            'type':'dataType + controlCode',
            'data':{

            }
        }
        :return:
        '''
