#  创建一个猫类
class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


#   创建一个猫对象
tom = Cat()
tom.drink()
tom.eat()

print(tom)
print("%d" % id(tom))
print("%x" % id(tom))

