name = "大明"
print("我的名字是：%s" % name)
print("我的名字是:  {}".format(name))

student_number = 201803020001
print("我的学号是：%d" % student_number)
price = 9
weight = 5
money = price * weight
print("苹果的单价是：%.02f元/斤,我购买了%.02f 斤,一共消费了：%.02f元" % (price, weight, money))
print("苹果的单价是：%.02f元/斤,我购买了%.02f 斤,一共消费了: %.02f元" % (price, weight, money))
print("苹果的单价是：%.02f元/斤，我购买了%.02f斤，一共消费了：%.02f元" % (price, weight, money))

ioney = float(input("请输入你的钱数："))
ioney = float(input("请输入你的钱数："))
print("%%")
scale = 0.81

print("数据比例是%.2f%%" % (scale * 100))

import keyword
print(keyword.kwlist)

