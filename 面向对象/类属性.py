class Tools:
    #  使用赋值语句定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name

        #  针对类属性做一个计数+1
        Tools.count += 1


#  创建工具对象

tool1 = Tools("榔头")
tool2 = Tools("斧头")
tools = Tools("铁锹")
print(Tools.count)
