import threading
from threading import Thread
import time


def task():
    time.sleep(3)
    print('子线程运行：名称为{}'.format(threading.currentThread().name))


thread_one = Thread(target=task)  # 创建前台线程
thread_two = Thread(target=task, daemon=True)  # 创建后台线程
