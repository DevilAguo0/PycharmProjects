class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        self.name = new_name

    def __del__(self):
        print("我走了")

    def __str__(self):
        return "我是小猫"

    def eat(self):
        print("{} 爱吃鱼".format(self.name))


#  使用类名创建对象的时候会自动调用初始化方法


tom = Cat("Tom")
tom.eat()
print(tom.name)
print("*" * 50)
print(tom)
# lazy_cat = Cat("大懒猫")
# print(lazy_cat.name)
# lazy_cat.eat()