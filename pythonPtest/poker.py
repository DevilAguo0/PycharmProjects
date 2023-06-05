import random

pc = ["方块", "红桃", "黑桃", "梅花"]
pv = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
poker = [c + v for c in pc for v in pv]
print(poker)
poker.extend(["大王", "小王"])
player1 = []
player2 = []
player3 = []
# print(poker)
# for i in range(53):
#     for j in range(52):
#         poker[i],poker[j] = poker[j],poker[i]
for i in range(53):
    poker[random.randint(0, 53)], poker[random.randint(0, 52)] = poker[random.randint(0, 52)], poker[
        random.randint(0, 53)]
# print(poker)
for i in range(17):
    m = i * 3
    player1.append(poker[m])
    player2.append(poker[m+1])
    player3.append(poker[m+2])
# print(poker)

poker_3 = poker[51:]
# print(poker_3)
a = random.randint(1,3)
if a == 1:
    player1.extend(poker_3)
elif a == 2:
    player2.extend(poker_3)
elif a == 3:
    player3.extend(poker_3)
print(player1)
print(player2)
print(player3)


