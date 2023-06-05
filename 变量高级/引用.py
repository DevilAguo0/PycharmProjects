def demo(num):
    # print("{}的地址是{}".format(num, id(num)))
    result = "hello"
    print("函数要返回数据的内存地址是{}".format(id(result)))
    return result


a = 10
print("a保存变量的地址是{}".format(id(a)))

# demo(a)
b = demo(a)
print("b保存变量的地址是{}".format(id(b)))
