# 2、给定两个非负整数m和n，编写函数计算组合数。计算组合数的
# 公式是=n!/(m!*(n-m)!)
def jie_cheng(num):
    if num == 1:
        return 1
    else:
        return jie_cheng(num-1)*num
def zu_he(m,n):

    return jie_cheng(n) / (jie_cheng(m)*jie_cheng(n-m))
print(zu_he(2,3))