try:
    num = int(input("请输入一个整数："))
    result = 8 / num
    print(result)

except ValueError:
    print("请重新输入一个整数！")

except Exception as erro:
    print("未知错误：{}".format(erro))
else:
    print("恭喜输入正确！")
finally:
    print("无论是否有异常都会被执行的代码")