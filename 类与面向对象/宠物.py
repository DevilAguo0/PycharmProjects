import math
class Circle(object):
    def __init__(self, r):
        self.r = r

    def area(self):
        area = math.pi * self.r*self.r
        # print("{:.2f}".format(area))
        # return area


c1 = Circle(3)
# Cicle.area()
# print(c1.area())
print(c1.area())