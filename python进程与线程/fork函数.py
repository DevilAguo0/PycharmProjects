import os
import time

value = os.fork()
if value == 0:
    print('--子进程1--')
    time.sleep(2)
    # print(os.getpid())
    # print(os.getppid())

else:
    print('--父进程2--')
    time.sleep(2)

    # print(os.getpid())
    # print(os.getppid())
value = os.fork()
if value == 0:
    print('--进程3--')
    time.sleep(2)

else:
    print('--进程4--')
    time.sleep(2)

