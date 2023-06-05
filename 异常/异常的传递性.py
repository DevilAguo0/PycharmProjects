#  避免在函数内部编写大量的捕获异常代码，在主程序中利用异常的传递性就可以捕获异常
def demo():
    return int(input("请输入一个整数："))


def demo2():
    return demo()


# print(demo2())
#  下面是主程序
try:
    print(demo2())
except Exception as result:
    print("未知错误{}".format(result))
