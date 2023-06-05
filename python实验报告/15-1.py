import random
import turtle
distance = random.randint(50, 150)
def star(distance):
    distance = random.randint(50, 150)
    turtle.penup()
    turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(distance)
        turtle.left(144)
        turtle.fillcolor(random.choice(["red", "blue", "yellow", "gray"]))
    turtle.end_fill()
    turtle.penup()
    turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
    star(distance)
    turtle.done()
star(distance)


