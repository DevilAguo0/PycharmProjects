class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("{}正在营业中".format(self.restaurant_name))

resturant = Restaurant("龙湖餐厅","hai")
resturant.describe_restaurant()
resturant.open_restaurant()
resturant.number_served = 20
print(resturant.number_served)

class IceCreamStand (Restaurant):
    def __init__(self,retaurant_name="龙湖",cursine_type="hai"):
        super().__init__(retaurant_name,cursine_type)
        self.flavors=["草莓","咖啡","苹果","原味"]
    def pri(self):

        print(self.flavors)

IceCreamStand = IceCreamStand()
IceCreamStand.pri()



