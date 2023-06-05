#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import sys
import threading
import queue

q = queue.Queue()

class PortScancer(threading.Thread):
    def __init__(self, host):
        super().__init__()
        self.host: str = host

    def run(self) -> None:
        while True:
            port = q.get()
            self.scanner(port)
            q.task_done()

    def scanner(self, port):
        conn = socket.socket()

        try:
            conn.connect((self.host, port))
            print("{} is open".format(port))

        except:
            pass


if __name__ == '__main__':
    host = sys.argv[1]
    ip = socket.gethostbyname(host)
    startPort = sys.argv[2]
    endPoet = sys.argv[3]
    threadNum = sys.argv[4]

    for i in range(int(threadNum)):
        t = PortScancer(ip)
        t.setDaemon(True)
        t.start()

    for i in range(int(startPort), int(endPoet)):
        q.put(i)

    q.join()
