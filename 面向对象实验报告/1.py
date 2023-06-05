import math


class Cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def area(self):
        area = math.pi * self.r * self.r * self.h
        print("圆柱的体积是{:.2f}".format(area))


cycle = Cylinder(2, 2)
cycle.area()
