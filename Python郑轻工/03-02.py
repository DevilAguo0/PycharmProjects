a = int(input())
b = []
for k in range(2, a):
    for i in range(2, k):
        if k % i == 0:
            # print("NO")
            break
    else:
        if a % k == 0:
            b.append(k)
            b.append(a / k)
print(int(max(b)))
