str = input("")
str_list = str.split()
x = int(str_list[0])
n = int(str_list[1])
print((x +1)**n)

#   #在python里是注释。
a, b = input().split()  # 输入，split()函数可以获得两个用空格分开的字符串并赋值给a,b。
a = int(a)  # 把a,b定义为int。
b = int(b)
print((a + 1) ** b)  # 直接输出a+1的b次方就行了（非常简单的数学题，不会的话可以看看别的题解）。
