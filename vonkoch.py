import turtle as t

t.penup()
t.goto(-100, 0)
t.pendown()
t.setheading(0)
t.hideturtle()
t.speed(0)
t.color('blue')
t.pensize(3)

def flocon(n, cote):
    if n==0:
        t.forward(cote)
    else:
        flocon(n-1, cote/3)
        t.left(60)
        flocon(n-1, cote/3)
        t.right(120)
        flocon(n-1, cote/3)
        t.left(60)
        flocon(n-1, cote/3)

for i in range(12):
    flocon(4, 500)
    t.right(120)
