import turtle
import math

turtle.penup()
product_list = []
revenue_list = []
Radius = 100
Total_Price = 0
turtle.speed(0)
preangle = 0
narc = 0
colours = ['red','yellow','blue','green','orange','pink']

def float_range(start, stop, step):
    while start < stop:
        yield start
        start += step

def Circle2_0(radiusL, angleL):
    turtle.pendown()
    position = turtle.position()
    turtle.forward(radiusL)
    angleT = turtle.heading()
    for i in float_range(0,angleL,0.1):
        angleN = math.radians(angleT+i)
        x = math.cos(angleN)*radiusL
        y = math.sin(angleN)*radiusL
        turtle.goto(x,y)
    turtle.goto(position)
    turtle.penup()
    
products = int(input("enter the number of products: "))

for i in range(0,products):
    name = input("enter name of product: ")
    revenue = int(input("Enter revenue of product: "))
    product_list.append(name)
    revenue_list.append(revenue)
    Total_Price = Total_Price + revenue

for j in range(0,products):
    turtle.fillcolor(colours[j])
    angle = revenue_list[j]/Total_Price*360
    narc = preangle + angle/2
    preangle += angle
    turtle.begin_fill()
    Circle2_0(Radius,angle)
    turtle.end_fill()
    turtle.setheading(narc)
    turtle.forward(Radius+20)
    turtle.write(product_list[j], align='center', font=('Arial', 16, 'bold'))
    turtle.back(Radius+20)
    turtle.setheading(preangle)

    
