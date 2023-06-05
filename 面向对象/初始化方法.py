class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        self.name = new_name

    def eat(self):
        print("{} 爱吃鱼".format(self.name))


#  使用类名创建对象的时候会自动调用初始化方法


tom = Cat("Tom")
tom.eat()
# print(tom.name)
# lazy_cat = Cat("大懒猫")
# print(lazy_cat.name)
# lazy_cat.eat()