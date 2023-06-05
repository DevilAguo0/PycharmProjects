# row = 1
# while row <= 5:
#     print("*" * row)
#     row += 1
#
# print("*", end="---")
# print("*")
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")  # 这行代码的目的就是在一行星星打印完成之后添加换行
    row += 1
