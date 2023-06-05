# 找出下面的问题所在，并修改好。
# 下面这段代码是使用Python实现将列表中的数与它相邻的数求均值并输出。例如：
# ls = [15,8,7,9,8]
# 输出结果为：[11.5,10,8,8,8.5]
# 可以看出，中间的数是与其左右两个数一起求平均值，而第一个数和最后一个数则只与
# 其相邻的一个数求平均值。函数代码如下：
# def mid_mean(ls):
#     new_ls = []
#     for i in range(len(ls)):
#         new_item = (ls[i-1]+ls[i]+ls[i+1])/3
#         new_ls.append(new_item)
#     return new_ls
# 将ls = [15,8,7,9,8]
# 传入mid_mean()函数中会报错，请你帮忙解决。


def mid_mean(ls):
    new_ls = []
    a=(ls[0]+ls[1])/2
    b=(ls[-1]+ls[-2])/2
    for i in range(1,4):
        new_item = (ls[i - 1] + ls[i] + ls[i + 1]) / 3
        new_ls.append(new_item)
    new_ls.insert(0,a)
    new_ls.insert(-1,b)
    return new_ls


ls = [15, 8, 7, 9, 8]
try:
    print(mid_mean(ls))

except Exception as Error:
    print(Error)
