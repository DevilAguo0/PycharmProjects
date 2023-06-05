#  、创建一个People类，包含属性name、city，可以转换
#  为字符串形式（__str__），包含方法moveto(self,newcity),
#  可以按照city排序，创建4个对象，放到列表进行排序。
class People:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return self.name + "," + self.city

    def moveto(self, newcity):
        self.city = newcity


p1 = People("张三", "北京")
p2 = People("李四", "上海")
p3 = People("王五", "广州")
p4 = People("赵六", "深圳")
people = [p1, p2, p3, p4]
for p in people:
    print(p)
print("\n")
people.sort(key=lambda x: x.city)
for p in people:
    print(p)
