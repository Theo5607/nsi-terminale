def pile():#retourne une liste vide
    return[]
    
# vide
def vide(p):
    """
    renvoie True si la pile est videet False sinon"""
    return p==[]
    
# empiler
def empiler(p,x):
    "Ajoute l’élément x à la pile p"
    p.append(x)

# dépiler
def depiler(p):
    "dépile et renvoie l’élément au sommet de la pile p"
    assert not vide(p), "Pile vide"
    return p.pop()
    
#taille
def taille(p):
    return len(p)

#élément en haut de la pile
def sommet(p):
    return p[-1]
    
def verification(chaine):
    pile1 = pile()
    for car in chaine:
        if car == '(':
            empiler(pile1, 1)
        elif car == ')':
            if taille(pile1)==0:
                return False
            else:
                depiler(pile1)
    if taille(pile1)==0:
        return True
    else:
        return False
    
print(verification('coucou(((istopgj))'))