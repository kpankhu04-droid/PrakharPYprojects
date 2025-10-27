import math
import turtle

turtle.speed(0)

def float_range(start, stop, step):
    while start < stop:
        yield start
        start += step

def Circle2_0(radiusL, angleL):
    turtle.pendown()
    position = turtle.position()
    turtle.forward(radiusL)
    angleT = turtle.heading()
    print(angleT)
    for i in float_range(0,angleL,0.1):
        angleN = math.radians(angleT+i)
        x = math.cos(angleN)*radiusL
        y = math.sin(angleN)*radiusL
        print(x,y,angleT)
        turtle.goto(x,y)
    turtle.goto(position)
    turtle.penup()

turtle.setheading(150)
Circle2_0(150,150)
