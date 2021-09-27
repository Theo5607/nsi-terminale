import turtle as t

t.penup()
t.goto(-100, 0)
t.pendown()
t.setheading(0)
t.hideturtle()
t.speed(0)
t.color('blue')
t.pensize(3)

class Rectangle:
    
    def __init__(self,long,larg):
        self.longueur=long
        self.largeur=larg
    
    def perimetre(self):
        return self.longueur*2+self.largeur*2
        
    def surface(self):
        return self.longueur*self.largeur
        
def afficher(rectangle):
    for i in range(0,2):
        t.forward(rectangle.longueur)
        t.right(90)
        t.forward(rectangle.largeur)
        t.right(90)
    
rectangle1=Rectangle(100,50)
afficher(rectangle1)
t.exitonclick