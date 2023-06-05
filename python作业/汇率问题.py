#   根据当前汇率，编程解决“美元和人民币的相互兑换”这一问题的程序。
money = input("请依次输入币值和符号($/¥)：")

if "¥" in money:
    dollor = float(money[0]) / 6.8
    print("可兑换的美元为：{} $".format(dollor))
else:
    cny = float(money[0]) * 6.8
    print("可兑换的人民币为：{} ¥".format(cny))

