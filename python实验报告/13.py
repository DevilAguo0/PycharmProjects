#  提示用户从键盘上输入一个正整数n，使用小海龟在
#  屏幕上输出一个任意大小和颜色的正n边形
import turtle
n = int(input("请输入正整数n："))
for i in range(n):
    turtle.pendown()
    turtle.forward(50)
    angle = 180-180*(n-2)/n
    turtle.left(angle)
turtle.done()
