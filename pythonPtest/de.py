num_list = [1, 2, 3, 3, 4, 5, 6, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 33, 34, 67, 0, 78, 6765]
for i in num_list[::]:
    if i > 1:
        for k in range(2, i):
            if i % k == 0:
                break
        else:
            num_list.remove(i)
print(num_list)
