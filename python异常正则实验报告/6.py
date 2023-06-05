# 输入一行数据，其中包括用逗号分隔得到的至少5个数值型数据，放入
# 列表ls中，然后输出。要求：如果输入的数据不是数值，则捕获Value
# Error异常，显示“请输入数值型数据”；如果输入的数据项不足5个，则捕获
# AssertionError异常，显示“请输入至少5个数据”。
class AssertionError(Exception):
    def __init__(self, error="请输入至少5个数据"):
        super(AssertionError, self).__init__(error)


try:
    ls = []
    a = input().replace(",","")
    for i in a:
        ls.append(int(i))
    if len(ls) < 5:
        raise AssertionError

except ValueError:
    print("请输入数值型数据")
except AssertionError as Error:
    print(Error)
