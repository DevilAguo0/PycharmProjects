#  编写程序，输入一个正整数，输出该数的数根。数根可以通过把
#  一个数的各位上的数字加起来得到。如果得到的数是一位数，那
#  么这个数就是数根。如果结果是两位数或者包含更多位的数字，那
#  么就把这些数字加起来。如此进行下去，直到得到的是一位数为止
def root(n):
    num = 0
    for i in str(n):
        num = num + int(i)
    if num > 10:
        return root(num)
    return num

print(root(783909878))


