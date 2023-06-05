class HomeIterm:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:

    def __init__(self, hose_type, area):
        #  房子户型
        self.hose_type = hose_type
        #  房子面积
        self.area = area
        #  剩余面积
        self.free_area = area
        #  家具列表
        self.iterm_list = []

    def __str__(self):
        return ("户型：%s,面积：%.2f,剩余面积：%s，家具：%s" %
                (self.hose_type, self.area,
                 self.freearea, self.iterm_list))

    def add_item(self, item):
        #  判断家具的面积
        if item.area > self.free_area:
            print("%s 的面积太大了，无法添加" % item)
            return
        #  将家具的名称添加到列表中
        self.iterm_list.append(item.name)
        #  计算剩余的面积
        self.free_area -= item.area


# 创建家具
bed = HomeIterm("席梦思", 97.0)
sofa = HomeIterm("沙发", 2.0)
table = HomeIterm("桌子", 2.0)
print(bed)
print(sofa)
print(table)
#  创建房子
guoshuaihao = House("两室一厅", 100)
guoshuaihao.add_item(bed)
guoshuaihao.add_item(sofa)
guoshuaihao.add_item(table)
