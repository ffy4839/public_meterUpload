from function import *
import time
import binascii
from Crypto.Cipher import AES
import pprint
import sys


HOST = ''
PORT = 8073
print([i for i in dir(AES) if not i.startswith('_')])

KEY = {
    '00':'01 02 03 04 05 06 07 08 00 00 00 00 00 00 00 00',
    '08':'80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
}




