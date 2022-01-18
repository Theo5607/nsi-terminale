def creation_arbre(r,profondeur):
    """ r : la racine (str ou int). la profondeur de l’arbre (int)"""
    Arbre = [r]+[None for i in range(2**(profondeur+1)-2)]
    return Arbre
def insertion_noeud(arbre,n,fg,fd):
    """Insére les noeuds et leurs enfants dans l’arbre"""
    indice = arbre.index(n)
    arbre[2*indice+1] = fg
    arbre[2*indice+2] = fd

def parent(arbre,p):
    if p in arbre:
        indice = arbre.index(p)
    if indice%2 == 0:
        return arbre[(indice-2)//2]
    else:
        return arbre[(indice-1)//2]

def est_vide(arbre):
    return (len(arbre)==0)

def enfants(arbre,n):
    indice = arbre.index(n)
    return (arbre[2*indice+1],arbre[2*indice+2])

def fils_gauche(arbre,n):
    indice = arbre.index(n)
    return arbre[2*indice+1]

def fils_droit(arbre,n):
    indice = arbre.index(n)
    return arbre[2*indice+2]

def est_racine(arbre,n):
    indice = arbre.index(n)
    return (indice==0)

def est_feuille(arbre,n):
    p=0
    while len(arbre)>2**p:
        p+=1
    indice = arbre.index(n)
    for i in range(len(arbre)-2**p-1,len(arbre)):
        return (indice==i)

def a_frere(arbre,n):
    

# création de l’arbre
arbre = creation_arbre("r",5)
# ajout des noeuds par niveau de gauche à droite
insertion_noeud(arbre,"r","a","b")
insertion_noeud(arbre,"a","c","d")
insertion_noeud(arbre,"b","e","f")
insertion_noeud(arbre,"c",None,"h")
insertion_noeud(arbre,"d","i","j")
insertion_noeud(arbre,"e","k",None)
insertion_noeud(arbre,"f",None,None)
insertion_noeud(arbre,"h",None,None)
insertion_noeud(arbre,"i",None,None)
insertion_noeud(arbre,"j","m",None)
insertion_noeud(arbre,"k",None,None)
insertion_noeud(arbre,"m",None,None)
#pour vérifier
print(len(arbre))
print(arbre)