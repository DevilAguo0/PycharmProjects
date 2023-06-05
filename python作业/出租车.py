#   3、本市出租车收费标准为：起步里程3公里，起步费13元；超起步里程后15公里内，
#   每公里2.3元；超过15公里以上部分加收50%的回空补贴费；停车等待3分钟内不收费，
#   超过3分钟的，每分钟按车公里价（即2.3元）的20%加收停车等候费。编写程序，输入
#   行驶里程数和停车等待时间，计算并打印乘客应付车费。

distance = float(input("请输入您的行驶里程数(单位公里)："))
time_wait = float(input("请输入您的停车等待时间(单位分钟)："))
if distance <= 3:
    if time_wait <= 3:
        print("乘客需要支付的车费为13元")
    else:
        expense = 13 + 2.3 * 0.2 * (time_wait - 3)
        print("乘客需要支付的车费为: {}元".format(expense))
elif 3 < distance <= 15:
    if time_wait <= 3:
        expense = 13 + (distance - 3) * 2.3
        print("乘客需要支付的车费为: {}元".format(expense))
    else:
        expense = 13 + (distance - 3) * 2.3 + (time_wait - 3) * 2.3 * 0.2
        print("乘客需要支付的车费为: {}元".format(expense))
else:
    if time_wait <= 3:
        expense = 13 + (distance - 3) * 2.3 + (distance - 15) * 0.5 * 2.3
        print("乘客需要支付的车费为: {}元".format(expense))
    else:
        expense = 13 + (distance - 3) * 2.3 + (time_wait - 3) * 2.3 * 0.2 + (distance - 15) * 0.5 * 2.3
        print("乘客需要支付的车费为: {}元".format(expense))
