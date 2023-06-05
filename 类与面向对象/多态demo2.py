class Animals:
    def __init__(self, age):
        self.age = age
        print("创建对象")

    def __del__(self):
        print("删除啦")

    def print_info(self):
        print("我今年{}岁了".format(self.age))


class Birds(Animals):
    def __init__(self, age, color):
        self.color = color

    def print_info(self):
        print("鸟类")
        super().print_info()


class Fish(Animals):
    def __init__(self, age, weight):
        self.weight = weight

    def print_info(self):
        print("鱼类")
        super().print_info()


A = Animals(23)
# B = Animals(23)
# A.name = "animals"
# print(B.name)
# print(isinstance(A, Animals))  # 判断是否为是实例化对象


















# 私有属性，私有方法
# __+name

# 类属性
# 实例属性
# 类方法
# 实例方法self


# 类方法
# 静态方法








