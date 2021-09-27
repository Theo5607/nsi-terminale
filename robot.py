import turtle as t

t.penup()
t.goto(-100, 0)
t.left(90)
t.pendown()
t.setheading(0)
t.speed(0)
t.color('blue')
t.pensize(3)

class Robot:
    
    def __init__(self,coor,dir):
        self.x=coor[0]
        self.y=coor[1]
        self.direction=dir
    
    def avancer(self):
        t.goto(self.x,self.y)
        angle=self.direction
        t.right(angle)
        t.forward(100)
        t.left(angle)
        
robot1=Robot((0,0),90)
robot1.avancer()