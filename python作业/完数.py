#  5、一个数如果恰好等于它的因子之和，这个数就称为"完数"。（例如 6 = 1＋2＋3）输入一个正整数n
# （n<1000），输出1到n之间的所有完数（包括n）。
# n = int(input("请输入任意一个数字n（n<1000）:"))
# for i in range(1, n + 1):
#     for k in range(1, int(i / 2) + 1):
#         result = 0
#         if i % k == 0:
#             result += k
#             if result == i:
#                 print(i)
#
num = int(input("请输入1000以内的任意一个数："))
for x in range(1, num + 1):
    sum = 0
    for y in range(1, int(x / 2) + 1):
        if x / y == int(x / y):
            sum = sum + y
    if sum == x:
        print(x)
