"""
一个对象的属性可以是
另一个类创建的对象
"""


# 枪类
class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        #  判断子弹数量
        if self.bullet_count <= 0:
            print("%s 里面没有子弹了" % self.model)
            return
            #  发射子弹-1
        self.bullet_count -= 1
        #  提示发射信息
        print("用 %s....突突突。。。现在还剩余 %d 发子弹" % (self.model, self.bullet_count))


#  士兵类
class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        #  判断是否有枪
        if self.gun is None:
            print("%s 还没有枪" % self.name)
            return
        #  喊口号
        print("冲啊！%s" % self.name)
        #  装子弹
        self.gun.add_bullet(50)
        # 扣动扳机
        self.gun.shoot()
        # 输出信息
        print("{}正在用{}攻打敌人，他现在还剩余 {} 发子弹了".format(self.name, self.gun.model, self.gun.bullet_count))


#  创建士兵
xusanduo = Soldier("许三多")
# 创建枪
Ak47 = Gun("Ak47")
xusanduo.gun = Ak47  # 在外部修改类属性，采用直接复赋值的方法
xusanduo.fire()
print(xusanduo.gun)
