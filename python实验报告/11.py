#  使用time函数库中的函数求当前系统的日期，并计算当前日期是本年度的第几天
import time
ticks = time.time()
localtime = time.localtime(ticks)
print(localtime)
print(time.asctime(localtime))
print(time.localtime())