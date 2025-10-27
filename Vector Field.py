import turtle as tl
import numpy as np

tl.penup()
tl.speed(0)
tl.pensize(2)
tl.shape('arrow')

print("enter 0 for no particle")

particle1 = int(input("enter the charge of your first particle: "))
print('')
print("must be within a grid of 700 by 700")
particle1POSX = int(input("enter the position of your first particle(x): "))
particle1POSY = int(input("enter the position of your first particle(Y): "))
    
print('')

particle2 = int(input("enter the charge of your second particle: "))
print('')
print("must be within a grid of 700 by 700")
particle2POSX = int(input("enter the position of your second particle(x): "))
particle2POSY = int(input("enter the position of your second particle(Y): "))

particle2POS = np.array([particle2POSX,particle2POSY])
particle1POS = np.array([particle1POSX,particle1POSY])

def draw_vector(pos1,p1,pos2,p2):
    E1 = np.array([0,0])
    E2 = np.array([0,0])
    x, y = tl.pos()
    cord = np.array([x,y])
    false_cord = np.array([0,0])
    if not (np.array_equal(cord, pos1) and p1 != 0) and not (np.array_equal(cord, pos2) and p2 != 0):
        if p1 !=0 :
            # calculates E1
            R1 = cord - pos1
            r1 = np.linalg.norm(R1)
            r1_hat = R1/r1
            E1 = (9*p1/r1**2)*r1_hat
        if p2 != 0:
            # calculates E2
            R2 = cord - pos2
            r2 = np.linalg.norm(R2)
            r2_hat = R2/r2
            E2 = (9*p2/r2**2)*r2_hat
        #calculates direction
        E_net = E1+E2
        Radians = np.arctan2(E_net[1], E_net[0])
        angle_deg = np.degrees(Radians)
        # moves the turle
        tl.setheading(angle_deg)
        tl.stamp()

def draw_plus():
    tl.setheading(0)
    tl.pendown()
    for _ in range(2):
        tl.forward(5)
        tl.backward(10)
        tl.forward(5)
        tl.left(90)
    tl.penup()

def draw_minus():
    tl.setheading(0)
    tl.pendown()
    tl.forward(5)
    tl.backward(10)
    tl.penup()



def P1():
    tl.goto(particle1POSX,particle1POSY)
    if particle1 > 0:
        tl.setheading(270)
        tl.forward(20)
        tl.setheading(0)
        tl.pendown()
        tl.fillcolor("red")
        tl.begin_fill()
        tl.circle(20)
        tl.end_fill()
        tl.penup()
        tl.goto(particle1POSX,particle1POSY)
        draw_plus()
        tl.penup()
    if particle1 < 0:
        tl.setheading(270)
        tl.forward(20)
        tl.setheading(0)
        tl.pendown()
        tl.fillcolor("blue")
        tl.begin_fill()
        tl.circle(20)
        tl.end_fill()
        tl.penup()
        tl.goto(particle1POSX,particle1POSY)
        draw_minus()
        tl.penup()

def P2():
    tl.goto(particle2POSX,particle2POSY)
    if particle2 > 0:
        tl.setheading(270)
        tl.forward(20)
        tl.setheading(0)
        tl.pendown()
        tl.fillcolor("red")
        tl.begin_fill()
        tl.circle(20)
        tl.end_fill()
        tl.penup()
        tl.goto(particle2POSX,particle2POSY)
        draw_plus()
        tl.penup()
    if particle2 < 0:
        tl.setheading(270)
        tl.forward(20)
        tl.setheading(0)
        tl.pendown()
        tl.fillcolor("blue")
        tl.begin_fill()
        tl.circle(20)
        tl.end_fill()
        tl.penup()
        tl.goto(particle2POSX,particle2POSY)
        draw_minus()
        tl.penup()

P1()
P2()

tl.pensize(4)
tl.fillcolor('purple')

for i in range(0,20):
    y = 350 - 35*i
    for j in range(0,20):
        x = (-350) + 35*j
        tl.goto(x,y)
        draw_vector(particle1POS,particle1,particle2POS,particle2)
        
