import random
player = int(input("请输入您的数字(石头(1)剪刀(2)布(3))："))
# if player != random.randint(1, 3):
#     print("不按照套路出牌！")

computer = random.randint(1, 3)
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家获胜")
elif player == computer:
    print("平局")
else:
    print("决战到天明")
