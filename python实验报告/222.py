import random
import turtle

m = random.randint(-300, 300)
n = random.randint(-300, 300)
x = random.randint(-300, 300)
y = random.randint(-300, 300)
distance = random.randint(50, 150)
color = random.choice(["red", "blue", "yellow", "gray"])


def star(m, n, distance, color):
    m = random.randint(-300, 300)
    n = random.randint(-300, 300)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    distance = random.randint(50, 150)
    color = random.choice(["red", "blue", "yellow", "gray"])
    turtle.penup()
    turtle.goto(m, n)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(distance)
        turtle.left(144)
        turtle.fillcolor(color)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x, y)
    star(m, n, distance, color)
    turtle.done()


star(m, n, distance, color)
