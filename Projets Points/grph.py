import matplotlib.pyplot as plt
from random import *
from turtle import *

def point(trt,x,y):
    trt.penup()
    trt.setx(x)
    trt.sety(y)
    trt.dot()

def pointil_vers(trt,p1,p2):
    '''
    fonction permettant de dessiner une ligne VERTICALE en pointillés entre 2 points
    '''
    trt.penup()
    trt.goto(p1)
    trt.seth(90)
    dif = p2[1]-p1[1]
    dif//4
    for i in range (int(dif//4)):
        trt.forward(4)
        trt.dot(2, "blue")



          
liste_points = []
x_max=int(input("Donnez une abcisse maximum: "))
y_max=int(input("Donnez une ordonnée maximum: "))
n=int(input("Donnez un nombre n de points: "))

for i in range(n):
    liste_points.append((randint(0, x_max), randint(0, y_max)))

setup(x_max, y_max)
turt = Turtle()
turt.ht()  
turt.penup()
turt.setx(0-(x_max/2))
turt.sety(0-(y_max/2))
turt.pendown()
turt.goto((x_max/2),0-(y_max/2))
turt.goto((x_max/2),(y_max/2))
turt.goto(0-(x_max/2),(y_max/2))
turt.goto(0-(x_max/2),0-(y_max/2))
turt.penup()
turt.goto(0,0-(y_max/2))
turt.pendown()
turt.goto(0,(y_max/2))

pointil_vers(turt,(40,0-(y_max/2)),(40,(y_max/2)))

turt.color("blue")
for el in liste_points:
    point(turt,el[0]-(x_max/2),el[1]-(y_max/2))

exitonclick()