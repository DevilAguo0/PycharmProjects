class Dog(object):

    def __init__(self, name):
        self.name = name

    def play(self):
        print("{}愉快的玩耍".format(self.name))


class XiaoTianDog(Dog):
    def play(self):
        print("{}飞到天上去玩耍".format(self.name))


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s和%s愉快的玩耍" % (self.name, dog.name))
        dog.play()


#  创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")
# xtq = XiaoTianDog("wangcai")
# dog.play()
#  创建一个小明对象
xiaoming = Person("小明")
#  让小明和狗一起玩耍
xiaoming.play_with_dog(wangcai)
