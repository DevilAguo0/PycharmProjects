year = int(input("请输入年份："))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400:
            print("是闰年")
    else:
        print("是闰年")
else:
    print("不是闰年")
