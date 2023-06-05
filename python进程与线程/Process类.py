from multiprocessing import Process
import os
import time


#
# def do_task():
#     print('子进程运行{}'.format(os.getpid()))
#
#
# process = Process(target=do_task)


class Myprocess(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        time_start = time.time()
        time.sleep(self.interval)
        time_stop = time.time()
        print("子进程%s执行结束，耗时0.2%f" % (os.getpid(), time_stop - time_start))


if __name__ == "__main__":
    myprocess = Myprocess(5)
    myprocess.start()
