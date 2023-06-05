# python port scanner
# !/usr/bin/env python3
# Path: awscode.py
# python port scanner

import socket
import sys
from threading import Thread


def connect_to_host(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(b'Hello, world!')
        print('%d open' % port)
    except:
        pass
    finally:
        s.close()


def main():
    if len(sys.argv) < 2:
        print('Usage: %s host' % sys.argv[0])
        exit(1)
    host = sys.argv[1]
    for port in range(1, 1024):
        t = Thread(target=connect_to_host, args=(host, port))
        t.start()


if __name__ == '__main__':
    main()
    exit(0)


# !/usr/bin/env python3
# Path: awscode.py
# python port scanner


def connect_to_host(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(b'Hello, world!')
        print('%d open' % port)
    except:
        pass
    finally:
        s.close()


def main():
    if len(sys.argv) < 2:
        print('Usage: %s host' % sys.argv[0])
        exit(1)
    host = sys.argv[1]
    for port in range(1, 1024):
        t = Thread(target=connect_to_host, args=(host, port))
        t.start()


if __name__ == '__main__':
    main()
    exit(0)
