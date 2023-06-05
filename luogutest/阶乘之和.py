n = int(input())
num_list = []
S = 0
b = 1
for i in range(1, n + 1):
    b = b * i
    num_list.append(b)
for i in num_list:
    i = int(i)
    S = S + i
print(S)


