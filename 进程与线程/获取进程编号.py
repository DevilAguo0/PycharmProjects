import time
from multiprocessing import Process
import os


def sing(num, name):
    print("sing进程的pid", os.getpid())
    print("sing进程的父进程的pid", os.getppid())

    for i in range(num):
        print(name)
        print("唱歌..")
        time.sleep(0.5)


def dance(num, name):
    print("dance进程的pid编号", os.getpid())
    print("dance进程的父进程的pid编号", os.getppid())

    for i in range(num):
        print(name)
        print("跳舞..")
        time.sleep(0.5)


if __name__ == '__main__':
    print("主进程的pid", os.getpid())
    #  使用进程类创建进程对象
    #  target = 指定进程的函数名
    #  args 以元组传参,要按照顺序传递参数
    #  kwargs 以字典传参，不用按照顺序传递参数，不过一定要保证key的存在
    sing_process = Process(target=sing, args=(7, "xioaming"))
    dance_process = Process(target=dance, kwargs={"name": "好几百", "num": 7})
    #  使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()