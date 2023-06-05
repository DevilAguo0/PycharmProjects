a = float(input("请输入第1个数："))
b = float(input("请输入第2个数："))
c = int(input("请输入第3个数："))
# print(max(a, b, c))
if a > b:
    if a > c:
        print("最大数是{}".format(a))
    else:
        print("最大数是{}".format(c))
else:
    if b > c:
        print("最大数是{}".format(b))
    else:
        print("最大数是{}".format(c))
