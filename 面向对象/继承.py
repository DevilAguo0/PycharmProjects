class Animals:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


# class Dog(Animals):
#     def bark(self):
#         print("汪汪叫!")


# class XiaoTiaoQuan(Dog):
#     def fly(self):
#         print("我会飞")
#
#
# class Cat(Animals):
#     def catch(self):
#         print("抓老鼠")
#
#
# dog = XiaoTiaoQuan()
# dog.sleep()
# dog.run()
# dog.eat()
# dog.drink()
# dog.bark()
# dog.fly()
#
# # dog.catch  # 同下
# xtq = Cat()
#
#
# # cat.fly()  # 啸天犬继承自Animals ，而非Cat ，所以不能飞
#
#
# class dogg(Cat, XiaoTiaoQuan):
#     pass
#
#
# Dosssss = dogg()
# Dosssss.fly()
# Dosssss.catch()


class ww:
    def eat(self):
        print("a")


class bb(ww, Animals):
    def eaft(self):
        print("fff")


demo = bb()
demo.eat()

print(bb.__mro__)
