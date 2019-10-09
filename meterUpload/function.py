import threading
import time
import binascii
import pprint
import sys


def timeNow(st ='%Y-%m-%d %H:%M:%S'):
    return time.strftime(st, time.localtime(time.time()))