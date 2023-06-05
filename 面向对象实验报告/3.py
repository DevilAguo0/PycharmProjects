class Student:
    def __init__(self, name, age, Chinese, Math, English):
        self.name = name
        self.age = age
        self.Chinese = Chinese
        self.Math = Math
        self.English = English

    def get_name(self):
        return str(self.name)

    def get_age(self):
        return int(self.age)

    def get_course(self):
        return max(int(self.Chinese),int(self.Math),int(self.English))

s1=Student("郭帅豪",23,123,134,150)
s2=Student("高航",22,123,111,120)
print(s1.get_age())
print(s1.get_name())
print(s1.get_course())