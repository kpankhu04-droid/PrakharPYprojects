import turtle
turtle.penup()
colour = ["red","blue","orange","green","yellow"]

def bar(height):
    turtle.setheading(0)
    for i in range(0,2):
        turtle.left(90)
        turtle.pendown()
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(50)


turtle.goto(-300,-300)
turtle.pendown()
for i in range(0,10):
    turtle.pendown
    turtle.forward(50)
    turtle.stamp()

turtle.goto(-300,-300)
turtle.left(90)
for i in range(0,10):
    turtle.pendown
    turtle.forward(50)
    turtle.stamp()
turtle.goto(-300,-300)
turtle.setheading(0)

bars = int(input("enter the number if bars you want to enter: "))

for i in range(0, bars):
    turtle.fillcolor(colour[i])
    size = int(input("enter size of the bar: "))
    name = input("enter the name: ")
    turtle.forward(100)
    turtle.begin_fill()
    bar(size)
    turtle.end_fill()
    
