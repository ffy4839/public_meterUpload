from socket import *
from configs import *
from bin.dataProcess import dataProcess


class meterServer():
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen(5)

    def run(self):
        print('{} | Waitting For Connections ...'.format(timeNow()))
        t1 = threading.Thread(target=self.meter_connectinos, args=())
        t1.start()
        while True:
            conn, c_addr = self.sock.accept()
            if conn and c_addr:
                t = threading.Thread(target=self.connection, args=(conn, c_addr))
                t.start()



    def connection(self, conn, c_addr):
        print('{} | Connect From {}'.format(timeNow(), c_addr))

        process = dataProcess(conn, c_addr)
        process.connection()

        conn.close()
        print('{} | Connect {} Is Over'.format(timeNow(), c_addr))

    def meter_connectinos(self):
        base_time = time.time()
        while True:
            now_time = time.time()
            if now_time - base_time >= 15:
                base_time = now_time
                print('{} | 当前连接表具数量 --- {}'.format(timeNow(), str(int(threading.activeCount()) - 2)))