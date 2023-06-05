# 编写程序，从键盘输入两个数，调用函数得到两个数的最大公约数，
# 输出函数调用结果。（要求：非递归、递归）
#  非递归

result_list = []


def common(m, n):
    a = min(m, n)
    for i in range(1, a + 1):
        if m % i == 0 and n % i == 0:
            result_list.append(i)


common(300, 100)
print(max(result_list))

#  递归
