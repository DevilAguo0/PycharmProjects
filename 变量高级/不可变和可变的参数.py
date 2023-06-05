def demo(num, num_list):
    print("打印函数内部的代码")
    num = 99
    num_list = [1, 2, 3, 4]
    print(num)
    print(num_list)
    print("函数执行完成")


"""
在函数内部针对参数使用赋值语句，
不会修改到外部的实参里
"""

gl_num = 100  # 不可变类型
gl_num_list = [4, 5, 6]  # 可变类型

demo(gl_num, gl_num_list)
print("打印函数外部代码")
print(gl_num)
print(gl_num_list)
