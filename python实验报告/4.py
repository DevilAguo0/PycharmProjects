# 小球从100m的高度自由落下，每次落地后反弹回原高度的一半，再落下。
# 定义函数cal计算小球第n次落地时，共经过多少以及第n次反弹多高。定义
# 全局变量Sn和Hn分别存储小球经过的路程和第n次的高度。主函数输入n的值，并
# 调用cal函数计算输出Sn和Hn的值
Sn = 0
Hn = 0


def cal(n):
    global Hn, Sn
    Hn = 100 * 0.5 ** n
    i = 0
    while i < n:
        Sn += Hn
        i += 1
    print(Hn)
    print(Sn)


cal(3)