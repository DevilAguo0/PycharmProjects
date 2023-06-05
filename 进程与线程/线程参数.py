import time
import threading


def sing(num):
    for i in range(num):
        print("唱歌。。")
        time.sleep(1)


def dance(count):
    for i in range(count):
        print("跳舞。。")
        time.sleep(1)


if __name__ == '__main__':
    sing_threading = threading.Thread(target=sing, args=(3,))
    dance_threading = threading.Thread(target=dance, kwargs={"count": 3})
    sing_threading.start()
    dance_threading.start()