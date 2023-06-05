import time
import multiprocessing


def work():
    #  子进程工作两秒
    for i in range(10):
        print("working..")
        time.sleep(0.2)


if __name__ == '__main__':
    #  主进程工作1秒，会发现主进程结束之后子进程还没有结束
    work_proess = multiprocessing.Process(target=work)
    work_proess.start()
    time.sleep(1)
    print("主进程结束啦！")
