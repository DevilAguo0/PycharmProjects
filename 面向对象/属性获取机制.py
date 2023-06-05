class Tools(object):
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

#  python中的"属性"获取机制是：向上获取机制
print(tool1.count)
print(tool2.count)
print(tools.count)
