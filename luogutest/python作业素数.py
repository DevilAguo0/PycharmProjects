num_list = [1, 23, 34, 445, 5, 3, 6, 64, 4, 4]
for i in num_list:
    for k in range(2, i):
        if i % k == 0:
            pass
        else:
            num_list.pop(num_list.index(i))
