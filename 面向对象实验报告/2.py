import math


class Cirlinder:
    def __init__(self, r):
        self.r = r

    def long(self):
        long = 2 * math.pi * self.r
        print("周长为{:.2f}".format(long))

    def area(self):
        area = math.pi * self.r * self.r
        print("面积为{:.2f}".format(area))
r1=Cirlinder(5)
r2=Cirlinder(10)
r1.long()
r1.area()
r2.long()
r2.area()