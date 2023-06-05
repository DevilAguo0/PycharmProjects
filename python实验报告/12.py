# 使用小海龟，在屏幕上绘制一系列的同心圆，
# 并为这些同心圆填充上不同的颜色。
import turtle as t
import random

t.colormode(255)
t.speed(0)

for i in range(1, 100):
    t.pu()
    t.goto(0, -i * 10)
    t.pd()
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.circle(i * 10)
t.done()