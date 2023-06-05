#  定义一个函数：输入num可以获得从1加到num的和


def sum_numbers(num):

    #  先分析出来递归的出口
    if num == 1:
        return 1

    # 假设sum_numbers函数可以解决这个问题
    # sum_numbers 可以得出1加到(num - 1)的结果，
    # 而我们所需要的结果是获得从1加到num的和，所以应该再加上num
    
    temp = sum_numbers(num - 1)
    return temp + num


result = sum_numbers(998)
print(result)
