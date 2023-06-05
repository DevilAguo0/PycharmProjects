class User:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(self.first_name, self.last_name, self.gender, self.age)

    def greet_user(self):
        print("你好！{}".format(self.first_name))


guo = User("guo", "shuaihao", "male", 23)
guo.describe_user()
guo.greet_user()


class Admin(User):
    def __init__(self, first_name="guo", last_name="shuai", age=23,gender="male"):
        super().__init__(first_name, last_name,age)
        self.privileges = ["can add post", "can delete post"]
        self.Privileges = Privileges()
    def show_privileges(self):
        print(self.privileges)

class Privileges(Admin):
    def __init__(self, privileges):
        self.privileges = super().privileges

    def show_privileges(self):
        super().show_privileges()







Admin = Admin()
Admin.show_privileges()



