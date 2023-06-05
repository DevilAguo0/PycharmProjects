#  九九乘法表
row = 1
while row <= 9:
    cal = 1
    while cal < row:
        print("{}*{} ={}".format(cal, row, cal * row), end="\t")
        cal += 1
    print(" ")
    row += 1
print("end")
