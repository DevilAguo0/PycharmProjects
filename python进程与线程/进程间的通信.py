# 通过队列实现两个进程之间的数据共享
from multiprocessing import Process
from multiprocessing import Queue


def write(queue):
    count = 10
    queue.put(count, block=False)


def read(queue):
    print(queue.get(block=False))


if __name__ == '__main__':
    queue = Queue()
    process_one = Process(target=write, args=(queue,))
    process_another = Process(target=read, args=(queue,))
    process_one.start()
    process_another.start()
#TODO:email:clarenceguo2060@gmail.com
