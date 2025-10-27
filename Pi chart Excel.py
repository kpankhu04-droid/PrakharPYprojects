import turtle
import csv

PRODUCTS_list = []
product_list = []
revenue_list = []
products = 0
turtle.penup()
Radius = 100
Total_Price = 0
turtle.speed(5)

PRODUCTS = open('CARS.csv', 'r')
for line in PRODUCTS:
    Row = line.strip().split(',')
    PRODUCTS_list.append(Row)

for row in range(0,len(PRODUCTS_list)):
    product_list.append(PRODUCTS_list[row][0])
    products = products + 1

for row in range(0,len(PRODUCTS_list)):
    revenue_list.append(PRODUCTS_list[row][1])

for row in range(1,len(PRODUCTS_list)):
    Total_Price = Total_Price + int(PRODUCTS_list[row][1])
    print(Total_Price)

turtle.setposition(0,-Radius)
turtle.pendown()
turtle.circle(Radius)
turtle.penup()
turtle.setposition(0,0)

for j in range(1,products):
    angle = int(revenue_list[j])/Total_Price*360
    turtle.pendown()
    turtle.left(angle)
    turtle.forward(Radius)
    turtle.back(Radius)
    turtle.penup()
    turtle.right(angle/2)
    turtle.forward(Radius+30)
    turtle.write(product_list[j], font=('Arial', 16, 'bold'))
    turtle.back(Radius+30)
    turtle.left(angle/2)

turtle.done()
