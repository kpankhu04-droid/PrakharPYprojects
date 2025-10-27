import turtle
import math
turtle.penup()
turtle.speed(0)

Radius = 100
SF = 10

angle = math.radians(45)
a = math.cos(angle)*Radius*2/3
b = math.sin(angle)*Radius*2/3

for i in range(0,50):
    x = a*i/50
    y = a*i/50
    R = Radius/(i+1)*2
    turtle.goto(x,y-R)

    turtle.pendown()
    turtle.circle(R)
    turtle.penup()
turtle.done()
