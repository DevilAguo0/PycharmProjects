import time
from multiprocessing import Process


def sing(num):
    for i in range(num):
        print("唱歌..")
        time.sleep(0.5)


def dance(num):
    for i in range(num):
        print("跳舞..")
        time.sleep(0.5)


if __name__ == '__main__':
    #  使用进程类创建进程对象
    #  target = 指定进程的函数名
    #  args 以元组传参
    #  kwargs 以字典传参
    sing_process = Process(target=sing, args=(7,))
    dance_process = Process(target=dance, kwargs={"num": 7})
    #  使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()
