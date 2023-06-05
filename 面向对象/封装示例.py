class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字是{},我的体重是{} 公斤".format(self.name, self.weight)

    def run(self):
        print("{}爱跑步，跑步锻炼身体".format(self.name))
        self.weight -= 0.5

    def eat(self):
        print("{}是吃货，吃完在跑步".format(self.name))
        self.weight += 1


xiaoming = Person("小明", 75)
xiaoming.eat()
xiaoming.run()
print(xiaoming)

xiaomei = Person("小美", 45)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
print(id(xiaomei))
print(id(xiaoming))
