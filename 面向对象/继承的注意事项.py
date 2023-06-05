class Animals:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animals):
    def bark(self):
        print("汪汪叫!")


class XiaoTiaoQuan(Dog):
    def fly(self):
        print("我会飞")

    def bark(self):
        #  针对子类编写特有的代码
        print("叫的跟神一样！")
        #  调用父类中的方法
        super().bark()
        # 增加其他子类代码
        print("wehgovnkdmjoieklg")


xtq = XiaoTiaoQuan()
xtq.bark()
