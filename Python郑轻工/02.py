import random

num = []
N = int(input())
i = 0
while i < N:
    a = random.randint(1, 1000)
    i += 1
    num.append(a)
num = set(num)
num = list(num)
num.sort()
for i in num:
    print(i, end=" ")
