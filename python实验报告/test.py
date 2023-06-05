import turtle
import random

color_list = ["yellow", 'red', 'blue', 'pink']
for j in range(random.randint(5, 10)):
    size = random.randint(50, 100)
    color = color_list[random.randint(0, 3)]
    turtle.begin_fill()
    turtle.down()
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.penup()
    turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
    turtle.fillcolor(color)
    turtle.end_fill()
turtle.done()
