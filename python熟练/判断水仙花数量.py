# a = int(input("请输入第一个数字："))
# b = int(input("请输入第二个数字："))
# c = int(input("请输入第三个数字："))
# sum_3 = a ** 3 + b ** 3 + c ** 3
# result1 = a * 100 + b * 10 + c
# result2 = b * 100 + a * 10 + c
# result3 = c * 100 + a * 10 + b
# result4 = a * 100 + c * 10 + b
# result5 = b * 100 + c * 10 + a
# result6 = c * 100 + b * 10 + a
# if sum_3 in (result6, result5, result4, result3, result2, result1):
#     print("{},{},{}是水仙花数".format(a, b, c, ))
# else:
#     print("{},{},{}不是水仙花数".format(a, b, c, ))
# print(sum_3)



num = int(input("请输入一个三位数："))
a = num // 100
b = (num - 100 * a) // 10
c  = num % 10
if a ** 3 + b ** 3 + c ** 3 == num:
    print("这个数字是水仙花数")
else:
    print("这个数字不是水仙花数")









