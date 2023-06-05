class PetDog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def sit(self):
        print(self.name + "is sitting now")

    def roll_dog(self):
        print(self.name + "rolled over")


sit = PetDog("dahuang", 15)
sit.sit()
