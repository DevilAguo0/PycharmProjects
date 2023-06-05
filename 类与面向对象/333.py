class init:
    def __init__(self, addr, tel):
        self.__addr = addr
        self.tel = tel

    def show_info(self):
        print(f"地址:{self.__addr}")
        print(f"手机号:{self.tel}")


init = init("北京", "12345")
init.show_info()
print("我今年{}岁了".format(self.age))

