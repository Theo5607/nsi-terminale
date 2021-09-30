from turtle import *
speed(0)
#On trace les axes de coordonnnés
penup()
goto(-300,0)
pendown()
goto(300,0)#axe des abscisses
penup()
goto(0,-300)
pendown()
goto(0,300)#axe des ordonnées

class Carre:
    #Le sommet de coordonnées (X,Y) est le coin en bas à gauche du carré
    #Cote est la longueur du côté du carré
    def __init__(self,X,Y,Cote):
        self.x=X
        self.y=Y
        self.cote=Cote

    def dessine(self):
        penup()
        goto(self.x,self.y)
        pendown()
        left(90)
        for i in range(4):
            forward(self.cote)
            right(90)

    def perimetre(self):
        #Question 2 : Après avoir supprimé l'instruction pass, compléter cette méthode qui doit retourner le périmètre du carré
        return self.cote*4

class Point:
    def __init__(self,abscisse,ordonnee):
        self.x=abscisse
        self.y=ordonnee

    def dessine(self):
        penup()
        goto(self.x,self.y)
        pendown()
        dot("red")

    def estdanscarre(self,carre):
        #Question 3 : Après avoir supprimé l'instruction pass, compléter cette méthode qui doit retourner True si le point est dans le carré carre (qui est un objet de la classe Carre), et False sinon
        return (self.x>=carre.x and self.x<=carre.x+carre.cote) and (self.y>=carre.y and self.y<=carre.y+carre.cote)


Origine=Point(0,0)
Origine.dessine()

A=Point(25,75)
A.dessine()

B=Point(200,100)
B.dessine()

#Question 4
#Créer et dessiner les points C et D de coordonnées C(150,100) et D(0,-200)
C=Point(150,100)
C.dessine()

D=Point(0,-200)
D.dessine()

#Question 5
#Créer et dessiner le carré appelé carre1 qui aura pour coin en bas à gauche le point A et pour côté 150 pixels
carre1=Carre(A.x, A.y, 150)
carre1.dessine()

#Question 6
#Faire afficher dans la console le périmètre du carré carre1 ; on fera une phrase !
print("Le prérimètre de carre1 est de",carre1.perimetre())

#Question 7
#En utilisant la méthode estdanscarre, faire afficher dans la console True ou False suivant que la phrase "Le point C est dans le carré carre1" est vraie ou fausse
print("Le point C est dans le carre1:",C.estdanscarre(carre1))

penup()
goto(200,100)
pendown()
forward(10)
left(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)

#Question 8
#En utilisant une boucle for et la classe Carre, dessiner, en partant du point D, une figure identique à celle présente à l'écran (les 5 carrés imbriqués les uns dans les autres en partant du point B)
carre2=Carre(D.x, D.y, 10)
for i in range(5):
    carre2.dessine()
    carre2.cote+=10
    right(90)

#Question 9
#En utilisant une boucle for et la classe Carre, dessiner la figure symétrique par rapport à l'axe des ordonnées de celle présente à l'écran (les 5 carrés imbriqués les uns dans les autres en partant du point B)
carre3=Carre(200, -150, 10)
for i in range(5):
    carre3.dessine()
    carre3.cote+=10
    right(90)


exitonclick()

