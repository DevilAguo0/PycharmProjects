def demo(num_list):
    print("打印函数内部的代码")
    num_list.append(4)
    print("函数执行完成")
    print(num_list)


gl_num_list = [4, 5, 6]  # 可变类型
demo(gl_num_list)
print(gl_num_list)
