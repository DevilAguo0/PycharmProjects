# 编写程序，对除法运算的异常进行处理。如果输入的除数为0，则输出提示
# 信息“输入错误：除数不能为0”，如果输入的被除数或除数不是数字，则输出
# 提示信息“输入有误：”及异常信息。


try:
    a = int(input())
    b = int(input())
    result = a / b
except ZeroDivisionError:
    print("输入错误：除数不能为0")
except Exception as Error:
    print("输入有误：{}".format(Error))


