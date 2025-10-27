import turtle
import math
turtle.penup()
turtle.speed(3)

Radius = 100

for i in range(-10,10):
    angle = math.radians(9*i)
    x = math.cos(angle)*Radius
    y = math.sin(angle)*Radius
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.goto(-x,y)
    turtle.penup()

turtle.setposition(0,-Radius)
turtle.pendown()
turtle.circle(Radius)
