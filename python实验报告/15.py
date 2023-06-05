import turtle
def star(m,n):
    turtle.penup()
    turtle.goto(m,n)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(200)
        turtle.left(144)
        turtle.fillcolor("red")
    turtle.end_fill()
    turtle.penup()


    turtle.goto(20,80)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(100)
        turtle.left(144)
        turtle.fillcolor("blue")
    turtle.end_fill()
    turtle.penup()



    turtle.goto(-200,50)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(100)
        turtle.left(144)
        turtle.fillcolor("yellow")
    turtle.end_fill()
    turtle.penup()

    turtle.done()
star(200,30)
star(20,300)
