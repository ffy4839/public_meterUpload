from configs import *

class protocolFunction():
    def transfer_time(self, t, st = '%y%m%d%H%M%S', tost = '%Y-%m-%d %H:%M:%S'):
        return time.strftime(tost, time.strptime(t,st))

    def b2h(self, data):  # socket接收的字节字符串转为字符串对象
        return binascii.hexlify(data).decode().upper()

    def h2b(self, data):  # 字符串转为socket可发送的字节字符串
        return binascii.unhexlify(data.encode())

    def checkSum(self, data):
        data = data.replace(' ', '')
        check = 0x00
        for i in range(0, len(data), 2):
            check = int(data[i:(i + 2)], 16) + check
            if check > 0xff:
                check -= 0x100
        check_hex = hex(check)[2:]
        return check_hex.rjust(2,'0').upper()

    def AES_encrypt(self, text, key = KEY['00']):  # AES 加密
        if not text:
            return None
        key = binascii.unhexlify(key.replace(' ','').ljust(32,'0').encode('utf-8'))
        text = binascii.unhexlify(self.AES_enpadding(text).encode())
        mode = AES.MODE_ECB
        cryptos = AES.new(key, mode)
        cipher_text = cryptos.encrypt(text)
        return binascii.hexlify(cipher_text).decode().upper()

    def AES_decrypt(self, text, key = KEY['00']):  # AES 解密
        key = binascii.unhexlify(key.replace(' ','').ljust(32,'0').encode('utf-8'))
        if len(text)%2 != 0:
            print('data length Error')
            return False
        text = binascii.unhexlify(text.replace(' ','').encode())
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode)
        plain_text = cryptor.decrypt(text)
        res = binascii.hexlify(plain_text).decode().upper()
        res = self.AES_depadding(res)
        return res

    def AES_enpadding(self, text, mode = 16): #PKCS7Padding填充方式
        if not text:
            return None
        text = text.replace(' ','')
        L = int(len(text) / 2)
        m = L % mode  #余数
        if m != 0:
            x_hex = hex(mode-m)[2:].rjust(2,'0')
            padding = (mode - m) * x_hex
        else:
            padding = hex(mode)[2:] * mode
        text += padding
        return text.upper()

    def AES_depadding(self, text):
        text = text.replace(' ','')
        padding = text[-2:]
        paddings = text[-2 * int(padding, 16):]
        paddings_set = set([paddings[i:i+2] for i in range(0, len(paddings), 2)])

        if padding in paddings_set and len(paddings_set) == 1:
            res = text[:len(text) - 2 * int(padding, 16)]
        else:
            res = text
        return res

    def big_Endian(self, data):
        data = data.replace(' ','')
        res = ''
        for i in range(0, len(data), 2):
            res = data[i:i+2] + res
        return res

    def negative(self, data):
        int_data = int(data, 16)
        if int_data >= int('FF000000', 16):
            res = -1 * (int('FFFFFFFF', 16) - int_data + 1)
        else:
            res = int_data
        return res

    def unnegative(self, data, i = 2, n = 8):
        data = int(float(eval(data)) * 10 ** i)
        if  data < 0:
            data = int('F'*n, 16) + 1 - abs(data)
        return self.big_Endian(hex(data)[2:].rjust(n, '0'))
