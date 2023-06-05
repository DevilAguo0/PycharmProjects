class phones:
    def call(self):
        print("打电话")


class Iphone(phones):
    def call(self):
        print("用iphone打电话")


class Aphone(phones):
    def call(self):
        print("用Andriod打电话")


class Person:
    def use_phone_call(self,phones):
        phones.call()


person = Person()
Iphone = Iphone()
Aphone = Aphone()
person.use_phone_call(Iphone)
person.use_phone_call(Aphone)




