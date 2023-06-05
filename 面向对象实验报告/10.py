# 提示用户从键盘上输入一个正整数n，使用小海龟在屏幕上输出一个任意大小和颜色的正n边形。
# 小海龟的颜色和位置由用户指定。
# 请尝试使用填充和边框的方法。
import turtle
turtle.pensize(5)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.end_fill()
turtle.done()
