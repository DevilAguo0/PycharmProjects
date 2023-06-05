try:
    num = int(input("请输入一个整数："))
    result = 8 / num
    print(result)

except ValueError:
    print("请输入一个整数：")

except Exception as erro:
    print("未知错误：{}".format(erro))
