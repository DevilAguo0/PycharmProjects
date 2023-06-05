class People(object):
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return self.name

    def moveto(self, newcity):
        self.city = newcity


p1 = People("张三", "北京")
p2 = People("里斯本", "上海")
p3 = People("王武", "成都")
p4 = People("阿里巴巴", "深圳")

print(p1)