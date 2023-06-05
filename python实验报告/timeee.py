import os
import random
import sys
import time
import turtle

print("hello world!")
time.sleep(2)

localtime = time.localtime(time.time())
print(localtime)
print(time.time())
print(time.asctime(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# a="Sat Mar 28 22:24:24 2022"
# print(time.mktime(time.strptime(a,"%a %b %H:%M:%S %Y")))
print("hello python!")



