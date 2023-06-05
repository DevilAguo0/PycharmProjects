num_list = [1, 2, 3, 3, 4, 5, 6, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 33]
num_list2 = []
num_list3 = []
if 1 in num_list:
    num_list3.append(1)
for i in num_list:

    for k in range(2, i):
        if i % k == 0:
            num_list3.append(i)
            break
    else:
        pass
print(num_list3)
#         num_list2.append(i)
#
# for i in num_list2:
#     num_list.remove(i)
# print(num_list)
# print(num_list2)

