#  石头剪刀布
import random

player = int(input("请输入你的数字(【1】石头【2】剪刀【3】布："))
compuer = random.randint(1, 3)
if (player == 1 and compuer == 2) \
        or (player == 2 and compuer == 3) \
        or (player == 3 and compuer == 1):
    print("玩家获胜")
elif player == compuer:
    print("平局")
else:
    print("电脑获胜")
