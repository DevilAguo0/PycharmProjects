#  创建一个猫类
class Cat:

    def eat(self):
        print(" %s 爱吃鱼" % self.name)

    def drink(self):
        print("{}爱喝水".format(self.name))


#   创建一个猫对象
tom = Cat()
tom.name = "tom"

tom.drink()
tom.eat()
