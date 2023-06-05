num = int(input())
a_list = []
for i in range(2, num + 1):
    if num % i == 0:
        for k in range(2, i):
            if i % k == 0:
                break
        else:
            a_list.append(i)
a_list.sort()
for i in a_list:
    print(i, end=" ")
