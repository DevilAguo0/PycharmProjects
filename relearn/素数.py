num_list = [1, 2, 3, 5, 6, 7, 8, 9, 0, 23, 34]
for i in num_list[::]:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            num_list.remove(i)
    # else:
    #     num_list.append(1)
print(num_list)

