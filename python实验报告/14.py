# 使用小海龟，绘制一个风轮效果，其中，
# 每个风轮内角为45度，风轮边长150像素。

import turtle
# import turtle
#
# turtle.left(-30)
# turtle.fillcolor("blue")
# turtle.begin_fill()
# turtle.circle(60, 180)
# turtle.left(90)
# turtle.forward(120)
# turtle.end_fill()
#
# turtle.fillcolor("yellow")
# turtle.begin_fill()
# turtle.circle(60, 180)
# turtle.left(90)
# turtle.forward(120)
# turtle.end_fill()
#
# turtle.left(-90)
# turtle.fillcolor("red")
# turtle.begin_fill()
# turtle.circle(60, 180)
# turtle.left(90)
# turtle.forward(120)
# turtle.end_fill()
#
# turtle.left(180)
# turtle.fillcolor("white")
# turtle.begin_fill()
# turtle.circle(60, 180)
# turtle.left(90)
# turtle.forward(120)
#
# turtle.done()


import turtle as t

t.setup(650, 350, 200, 200)
t.seth(90)
t.fd(150)
t.seth(0)
t.circle(-150, 45)
t.goto(0, 0)
t.seth(0)
t.fd(150)
t.seth(270)
t.circle(-150, 45)
t.goto(0, 0)
t.seth(270)
t.fd(150)
t.seth(180)
t.circle(-150, 45)
t.goto(0, 0)
t.seth(180)
t.fd(150)
t.seth(90)
t.circle(-150, 45)
t.goto(0, 0)
