#  要求编写程序，开发猜数字小游戏。
#  计算机随机生成100以内的数字，玩家去猜，若猜测的数字大于生成的数字，
#  提示“很遗憾，你猜大了”；若猜测的数字小于生成的数字时，提示“很遗憾，你
#  猜小了”；直到猜中该数，显示“恭喜！你猜对了”，同时显示玩家猜的次数，并询
#  问玩家是否继续游戏，继续则输入“y”或“Y”，结束游戏则输入“n”或“N”。

import random
computer = random.randint(1, 100)
print(computer)
person = int(input("请随机输入一个100以内的整数："))

i = 0
while True:
    if person > computer:
        print("很遗憾猜大了！")
    elif person == computer:
        print("恭喜！你答对了")
        break
    else:
        print("很遗憾，你猜小了！")
    i += 1
    print("这是您猜的第{}次".format(i))
    print("")
    right = input("请问您是否继续（Y(y）/ N(n)：")
    if right == "Y" or right == "y":
        person = int(input("请随机输入一个100以内的整数："))
        i = 0
        while True:
            if person > computer:
                print("很遗憾猜大了！")
            elif person == computer:
                print("恭喜！你答对了")
                break
            else:
                print("很遗憾，你猜小了！")
            i += 1
            print("这是您猜的第{}次".format(i))
            print("")
            right = input("请问您是否继续（Y(y）/ N(n)：")
    else:
        break



