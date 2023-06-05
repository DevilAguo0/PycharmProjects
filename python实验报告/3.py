# 编写程序，求方程ax2+bx+c=0的根，用3个函数分别
# 求当b2-4ac大于0、等于0和小于0时的根。要求从主函
# 数输入a、b、c的值，输出方程的根。
def root(a, b, c):
    if b ** 2 - 4 * a * c > 0:
        print("x1={}".format((-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a))
        print("x2={}".format((-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a))
    elif b ** 2 - 4 * a * c == 0:
        print("x1=x2={}".format(-b / 2 * a))
    elif b ** 2 - 4 * a * c < 0:
        print("没有根")


root(1, 2, 1)
