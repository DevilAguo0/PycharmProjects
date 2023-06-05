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

#  直接增加属性，但是不推荐使用，利用赋值语句，属性名就可以了
tom.name = "tom"
print(tom.name)


lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
lazy_cat.name = "大懒猫"
lazy_cat.age = 18
print(tom)
print(lazy_cat)
print(lazy_cat.age)
