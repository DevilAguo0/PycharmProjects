su_num = []
num = int(input(""))
for k in range(2, num):
    if k != 1:
        for i in range(2, k - 1):
            if k % i == 0:
                break
        else:
            su_num.append(k)
    else:
        pass
k = 0
for i in su_num:
    if i + 2 in su_num:
        print(i, i + 2)
        k += 1
if k == 0:
    print("empty")
