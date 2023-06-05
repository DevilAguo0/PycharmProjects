from multiprocessing import Pool
import os
# pool = Pool(processes=5)
import time


def work(num):
    print('进程{}:执行任务{}'.format(os.getpid(), num))
    time.sleep(2)


if __name__ == '__main__':
    pool = Pool(3)
    for i in range(9):
        pool.apply_async(work, (i,))
        time.sleep(3)
        print('主进程执行任务')
    # pool.close()
    # pool.join()
