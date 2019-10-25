from function import *
import time
import binascii
from Crypto.Cipher import AES
import pprint
import sys


HOST = ''
PORT = 8073
# print([i for i in dir(AES) if not i.startswith('_')])

KEY = {
    '00':'01 02 03 04 05 06 07 08 00 00 00 00 00 00 00 00',
    '08':'80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
}

TRANSFORM_Z2E = {
    "表具编号":'meter_id',"表具类型":'meter_type',"客户编号":'user_num',
    "客户姓名":'user_name',"用气地址":'user_add',"上告时间":'updata_time',
    "累积总量":'cumulate_all',"标况总量":'cumulata_standard',"工况总量":'cumulata_work',
    "标况瞬时量":'flow_standard',"工况瞬时量":'flow_work',"温度":'temp',
    "压力":'pressure',"剩余金额":'balance',"当前单价":'price',
    "周期累积量":'cycle_cumulate',"锂/蓄电池电压":'power',
    "锂/蓄电池电量百分比":'power_percentage',
    "GPRS信号强度":'gprs_singer',"存储状态":'flash',"电压状态":'Voltage',
    "金额状态":'balance_status',"阀门状态":'valve',"开通状态":'open',
    "开盖状态":'cover',"断线状态":'line',"液晶状态":'display',
    "外供电状态":'out_power_status',"RS485状态":'rs485_status',"GPRS状态":'gprs_status',
    "阀门强制状态":'value_force',"计数方式":'count_type',"计量单位1":'count_unit_1',
    "计量单位2":'count_unit_2',"网络类型":'net_type',"流量计地址":'meter_addr',
    "流量计电池":'meter_power',"流量计状态":'meter_status',"声速":'sound_speed'
}
TRANSFORM_E2Z = {}
for key,value in TRANSFORM_Z2E.items():
    TRANSFORM_E2Z[value] = key



