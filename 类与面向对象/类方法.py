class Person(object):
    @classmethod
    def personal(cls):
        print("类方法")





p=Person()
p.personal()
print(Person.personal())




class Animal(object):
    @staticmethod
    def animal():
        print("静态方法")


a=Animal
a.animal()


自由方法不能通过对象调用，只能通过类名调用




