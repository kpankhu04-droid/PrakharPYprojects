import turtle
import math
turtle.penup()
turtle.speed(0)

Radius = 100
SF = 10

for i in range(0,(10*SF)+1):
    a = i/SF
    angle = math.radians(9*a)
    x = math.cos(angle)*Radius
    y = math.sin(angle)*Radius
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.goto(-x,y)
    turtle.goto(-x,-y)
    turtle.goto(x,-y)
    turtle.goto(x,y)
    turtle.penup()

turtle.setposition(0,-Radius)
turtle.pendown()
turtle.circle(Radius)
