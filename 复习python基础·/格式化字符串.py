a = 3.1415926
print("{:.2f}".format(a))
print("{:+.2f}".format(a))
print("{:.0f}".format(a))

b = 1
print("{:+.2f}".format(b))
print("{:.2f}".format(b))  # 重要
print("{:0<2d}".format(b))
print("{:0>2d}".format(b))
print("{:x>2d}".format(b))
c = 1000000
print("{:,}".format(c))
d = 0.25
print("{:.2%}".format(d))  # 重要
print("{:.2e}".format(c))
print("{:>10d}".format(c))
print("{:<10d}".format(c))
print("{:^10d}".format(c))






#  ^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
# + 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
# b、d、o、x 分别是二进制、十进制、八进制、十六进制。




print('{:b}'.format(11))
print('{:d}'.format(11))
print('{:o}'.format(11))
print('{:x}'.format(11))
print('{:#x}'.format(11))
print('{:#X}'.format(11))

#  此外我们可以使用大括号 {} 来转义大括号，如下实例：
print("{} 对应的位置是 {{0}}".format("runoob"))
