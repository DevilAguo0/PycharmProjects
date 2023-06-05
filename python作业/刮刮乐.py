import random

game = ["谢谢惠顾", "一等奖", "三等奖", "谢谢惠顾", "谢谢惠顾 ", "三等奖", "二等奖", "谢谢惠顾"]
i = 0
n = 7
while i < 7:
    a = random.randint(0, n)
    game.remove(a)
    print(game[a])
    n -= 1
    i += 1

print(game[a])
