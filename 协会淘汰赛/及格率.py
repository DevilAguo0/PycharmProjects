n = int(input())
scores = input().split()
print(n)
print(scores)
num = 0
for i in scores:
    if int(i) < 60:
        num += 1
result = num / (n - num)
print("{:.2f}".format(result))
