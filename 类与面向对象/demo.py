# class Person(object):
#     "这是一个测试类"
#     name = "python"
#
#
#
# print(Person.__doc__)
# print(type(Person))
# class PetDog(object):
#     def __int__(self,name,age):
#         self.name = name
#         self.age=age
#     def sit(self):
#         print(self.name+"is setting nowing")
#     def roll_over(self):
#         print(self.name+"rolled over.")
#
#
# # roll_over = PetDog.roll_over(roll)
# sitdog = PetDog()
# sitdog.sit()


class Cicle():
    def __init__(self, r):
        self.r = r

    def area(self):
        area = 3.14 * self.r * self.r
        print("{:.2f}".format(area))


cicle = Cicle(3)
cicle.area()
