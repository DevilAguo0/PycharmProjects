# 编程验证哥德巴赫猜想之一：任意一个大于2的偶数都可以表示成两个素数之和。
# 函数isGDBH(n)将传入的4-200之间的偶数表示为2个素数之和，结果保存在
# 列表中返回。例如，函数传入参数为10，则返回[“10=3+7”,“10=5+5”]。（
# 要求：定义必要的函数，使程序结构清晰）
result_list = []


def isGDBH(n):
    for i in range(2, n):
        if n % i != 0:
            for k in range(2, n - i):
                if (n - i) % k == 0:
                    break
            else:
                result_list.append("{}+{}={}".format(n, i, n - i))
    result_list.pop()
    return result_list


print(isGDBH(300))
