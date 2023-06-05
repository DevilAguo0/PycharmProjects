import time
import os
value = os.fork()
if value == 0:
    print("子进程")
else:
    print("父进程")
    time.sleep(2)
print (os.__file__)
