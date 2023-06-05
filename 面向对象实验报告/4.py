class Student:
    def __init__(self, name, age, chinese, math, english):
        self.name = name
        self.age = age
        self.Chinese = chinese
        self.Math = math
        self.English = english

    def get_name(self):
        return str(self.name)

    def get_age(self):
        return int(self.age)

    def get_course(self):
        return int(self.Chinese), int(self.Math), int(self.English)


class HighSchoolStudent(Student):
    def __init__(self, name, age, chinese, math, english, physics, chemical, biology, history, politics):
        super().__init__(name, age, chinese, math, english)
        self.Physics = physics
        self.Chemical = chemical
        self.Biology = biology
        self.History = history
        self.Politics = politics

    def get_average(self):
        tuple_subject = (
            self.Chinese, self.Math, self.English, self.Chemical, self.Physics, self.Biology, self.Politics)

        return sum(tuple_subject) / 8

    def get_course(self):
        return max(self.Chinese, self.Math, self.English, self.Chemical, self.Physics, self.Biology, self.Politics)


hss1 = HighSchoolStudent("郭帅豪", 22, 123, 123, 122, 90, 89, 90, 89, 78)
print("平均分为{:.2f}".format(hss1.get_average()))
print("最高分为{:.2f}".format(hss1.get_course()))
