import threading
import time


def work():
    for i in range(10):
        print("正在工作。。。")
        time.sleep(0.2)


if __name__ == '__main__':
    # 主线程结束不想等待子线程，可以设置守护，这是第一种方法
    # work_thread = threading.Thread(target=work, daemon=True)
    # work_thread.start()

    # work_thread = threading.Thread(target=work)
    # work_thread.start()

    # 下面是第二种方法，需要注意的是 一定要在任务start之前设置守护，否则会报错！
    work_thread = threading.Thread(target=work)
    work_thread.setDaemon(True)

    work_thread.start()
    time.sleep(1)
    print("主线程结束啦！")
