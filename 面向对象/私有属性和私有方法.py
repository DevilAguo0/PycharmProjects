class Woman:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("{}的年龄是{}".format(self.name, self.__age))


xiaomei = Woman("xiaomei")
#  私有属性在外界不能被访问
# print(xiaomei.__age)
# xiaomei.__secret()

#  伪私有属性和私有方法
xiaomei._Woman__secret()
print(xiaomei._Woman__age)
