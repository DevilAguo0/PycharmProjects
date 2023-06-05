list1 = []
num = int(input(''))

for i in range(2, num):
    while True:
        if num % i == 0:
            list1.append(i)
            num = num / i
        else:
            break
print(max(list1))