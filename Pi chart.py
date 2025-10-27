import turtle

turtle.penup()
product_list = []
revenue_list = []
Radius = 100
Total_Price = 0
turtle.speed(2)

products = int(input("enter the number of products: "))

for i in range(0,products):
    name = input("enter name of product: ")
    revenue = int(input("Enter revenue of product: "))
    product_list.append(name)
    revenue_list.append(revenue)
    Total_Price = Total_Price + revenue

turtle.setposition(0,-Radius)
turtle.pendown()
turtle.circle(Radius)
turtle.penup()
turtle.setposition(0,0)

for j in range(0,products):
    angle = revenue_list[j]/Total_Price*360
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
