num = int(input("请输入任意一个数字："))
if num != 1:
    for i in range(2, num-1):
        if num % i == 0:
            break
    else:
        print("是素数")
else:
    print("不是素数")
