import turtle as tl
import math

tl.penup()

H0 = 20
g = 9.8
choice = ''

while (choice != 'S') and (choice != 'F'):
    choice = (input("do you want to input speed or force(S or F): ")).upper()
    if choice == 'S':
        V = int(input("enter speed(m/s): "))
        R = int(input("enter the degree of release: "))
    elif choice == 'F':
        F = int(input("enter force(N): "))
        M = int(input("enter the mass of the turtle(kg): "))
        R = int(input("enter the degree or release: "))
        V = F/M
    elif (choice != 'S') and (choice != 'F'):
        print("invalid input")

def draw_man(x, y):
    tl.pensize(3)
    # Head (centered at x, y)
    tl.penup()
    tl.goto(x, y - 40)
    tl.pendown()
    tl.circle(20)
    # Body
    tl.penup()
    tl.goto(x, y - 40)
    tl.pendown()
    tl.goto(x, y - 100)
    # Arms
    tl.penup()
    tl.goto(x, y - 60)
    tl.pendown()
    tl.goto(x - 30, y - 80)
    tl.penup()
    tl.goto(x, y - 60)
    tl.pendown()
    tl.goto(x + 30, y - 80)
    # Legs
    tl.penup()
    tl.goto(x, y - 100)
    tl.pendown()
    tl.goto(x - 20, y - 140)
    tl.penup()
    tl.goto(x, y - 100)
    tl.pendown()
    tl.goto(x + 20, y - 140)
    tl.pensize(1)
    tl.penup()

V=V*1.5
angle = math.radians(R)
V_v = math.sin(angle)*V
V_h = math.cos(angle)*V
T = (V_v+math.sqrt((V_v**2)+(2*g*50)))/g
t_total = math.ceil(T)

tl.goto(-350,-100)
tl.pendown()
tl.goto(350,-100)
tl.penup()

draw_man(-325,30)

tl.goto(-300,-50)
for t in range(0, (t_total+11)*5, 1):
    t=t/5
    tl.pendown()
    H = (V_v*t)-(g*(t**2)/2)
    if H < -50:
        break
    D = V_h*t
    tl.goto(D-300,H-50)
    tl.penup()

H = (V_v*T)-(g*(T**2)/2)
D = V_h*T
tl.goto(D-300,H-50)

tl.shape("turtle")
tl.stamp()

tl.done()
