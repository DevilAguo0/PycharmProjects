# 3、假设成年人的体重和身高存在此关系：身高（厘米）-100=标准体重（千克）
# 如果一个人的体重与其标准体重的差值在正负5%之间，显示“体重正常”其他则显示“体重超标”
# 或不达标。编写程序，能处理用户输入的异常，并且使用自定义异常类来处理身高小于30cm，
# 大于250cm的异常情况。


class InputError(Exception):
    def __init__(self, error="输入异常"):
        super().__init__(error)


try:
    height = float(input("请输入身高(cm):"))
    weight = float(input("请输入体重(kg):"))
    if (height - 100) * 0.95 < weight < (height - 100) * 1.05:
        print("体重正常")
    else:
        print("体重超标")
    if height < 30 or height > 250:
        raise InputError

except InputError as Error:
    print(Error)
