import threading
import time


def task():
    time.sleep(1)
    thread = threading.current_thread()
    print(thread)


if __name__ == '__main__':
    for i in range(5):
        threading_proess = threading.Thread(target=task)
        threading_proess.start()
