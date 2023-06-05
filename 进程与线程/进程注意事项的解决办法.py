import time
import multiprocessing
# 利用os模块中的  ： 子进程对象.daemon = True 解决这个问题
import os


def work():
    for i in range(10):
        print("working..")
        time.sleep(0.2)


if __name__ == '__main__':
    work_proess = multiprocessing.Process(target=work)
    #  设置守护主进程，主进程结束，子进程自动销毁，不再执行子进程代码
    work_proess.daemon = True
    work_proess.start()
    time.sleep(1)
    print("主进程结束啦！")
