from math import *
from random import *
from copy import *

liste_points = []
x_max=int(input("Donnez une abcisse maximum: "))
y_max=int(input("Donnez une ordonnée maximum: "))
n=int(input("Donnez un nombre n de points: "))

for i in range(n):
    liste_points.append((randint(0, x_max), randint(0, y_max)))

def distance(p, q):
    vect=(q[0]-p[0],q[1]-p[1])
    return sqrt(vect[0]**2+vect[1]**2)

def distance_minimal_force_brute(pts):
    min=sqrt(x_max**2+y_max**2)
    for p1 in pts:
        for p2 in pts:
            dist=distance(p1, p2)
            if p1!=p2 and dist<min:
                min=dist
    return min

print(distance_minimal_force_brute(liste_points))
#il y a n**2 appels de la fonction distance

def trier(L, i):
    """
    Fonction de tri qui prend en paramètre une liste de tuples (ici de coordonnées de points),
    et un indice i correspondant à l'indice du tuple sur lequel effectuer le tri, et qui renvoie
    la liste triée selon cet indice.
    Cette fonction repose sur l'algorithme de tri rapide.
    """
    gauche = []
    egal = []
    droit = []
    if len(L)>1:
        pivot=L[0][i]
        for el in L:
            if el[i]<pivot:
                gauche.append(el)
            elif el[i]==pivot:
                egal.append(el)
            elif el[i]>pivot:
                droit.append(el)
        return trier(gauche, i) + egal + trier(droit, i)
    else:
        return L

px=trier(deepcopy(liste_points), 0)
py=trier(deepcopy(liste_points), 1)

def distance_minimal_dpr(px,py):
    long=len(px)
    px1=px[:long//2]
    px2=px[long//2:]
    if len(px1)<=1 or len(px2)<=1:
        return sqrt((px2[0][0]-px1[0][0])**2+(px2[0][1]-px1[0][1])**2)
    m=(px1[-1][0]+px2[0][0])//2
    return min(distance_minimal_dpr(px1, [el for el in py if el[1]<=m]), distance_minimal_dpr(px2, [el for el in py if el[1]>m]))

print(distance_minimal_dpr(px, py))