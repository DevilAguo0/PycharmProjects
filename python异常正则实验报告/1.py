# 1、编写一个存储学生成绩的小程序，如果输入的成绩小于0或大于100，
# 提示异常信息“输入有误，请输入正确的成绩信息”。如果输入的成绩在0~100
# ，则存储信息；如果输入的有效成绩达到5个，则退出程序并在控制台打印这5
# 个有效成绩。无论是否出现异常，都在控制台打印输出目前的时间戳

import time

score = []


class Information(Exception):
    def __init__(self, error="输入有误，请输入正确的成绩信息"):
        super().__init__(error)


while True:
    try:

        a = int(input())
        if a < 0 or a > 100:
            raise Information
    except:
        print("输入有误，请输入正确的成绩信息")
    else:
        score.append(a)
    finally:
        if len(score) == 5:
            for i in score:
                print(i, end=" ")
            print(time.time())
