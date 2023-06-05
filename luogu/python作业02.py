list2 = [2, 4, 6, 8, 10]
list3 = [1, 3, 5, 7, 9]
list4 = []
i = 0
while i < 5:
    result = list2[i] * 10 + list3[i]
    list4.append(result)
    i += 1
print(list4)


#  合并
# list2.extend(list3)
# print(list2)
list6 = list2 + list3
print(list6)