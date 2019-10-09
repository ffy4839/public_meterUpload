import serial
import time
import binascii
import re



def timen(d='%Y-%m-%d,%H:%M:%S'):
    return time.strftime(d, time.localtime(time.time()))


def print_save(data):
    print(data)


class ser(serial.Serial):
    def __init__(self,port):
        super(ser, self).__init__()
        self.port = port
        self.open_ser()
        self.parse_data = 'recv'

    def open_ser(self):
        self.baudrate = 9600
        self.timeout = 0.5
        self.open()

    def send(self, data):
        '''串口发送数据'''
        data = binascii.unhexlify(data)
        if self.is_open:
            try:
                self.flushOutput()
                self.write(data)
            except Exception as e:
                print('{};{},串口发送错误'.format(timen(), e))
                quit()
        else:
            self.open_ser()

    def recv(self, times=1):
        self.isopened()
        self.flushInput()
        while True:
            inwaiting = self.in_waiting
            if inwaiting:
                recv = self.read_all()
                self.recv_parse(recv)
            time.sleep(1)
        # recv_data_all = self.parse_data
        # self.parse_data = 'recv'
        # return

    def recv_parse(self, data, code='utf-8'):
        if code == 'utf-8':
            try:
                datas = binascii.hexlify(data).decode('utf-8').upper()
                re_com = re.compile('68.*16')
                datas = re.findall(re_com, datas)[0]
                print_save(' '*5+'|接收:'+datas)
            except:
                self.recv_parse(data,'ascii')

        if code == 'ascii':
            try:
                datas = data.decode('ascii')
                # self.parse_data += datas + '\n'
                print_save(' '*5+'|接收:'+datas)
            except:
                self.recv_parse(data,'GBK')

        if code == 'GBK':
            try:
                datas = data.decode('GBK').replace('\n','').replace('\r','')
                # self.parse_data += datas + '\n'
                print_save(' '*5+'|接收:'+datas)
            except:
                print_save(' '*5+'|接收:'+str(data))

    def sopen(self):
        if not self.is_open:
            self.open()

    def sclose_ser(self):
        if self.is_open:
            self.close()

    def isclosed(self):
        if self.is_open:
            self.close()

    def isopened(self):
        if not self.is_open:
            self.open()


if __name__ == '__main__':
    port = input()
    s = ser(port)

    s.recv()
