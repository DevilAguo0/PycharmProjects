import time
from multiprocessing import Process


def sing():
    for i in range(3):
        print("唱歌..")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("跳舞..")
        time.sleep(0.5)


if __name__ == '__main__':
    #  使用进程类创建进程对象，target 后面跟函数
    sing_process = Process(target=sing)
    dance_process = Process(target=dance)
    #  使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()
