# 给定两个整数m和n，求出m~n这段连续的整数中所有偶数的平方和以及所有奇数的立方和。
m, n = input().split()
m = int(m)
n = int(n)
result_01 = 0
result_02 = 0
for i in range(m, n + 1):
    if i % 2 == 0:
        result_01 = i ** 2 + result_01
    else:
        result_02 = i ** 3 + result_02

print(result_01)
print(result_02)




