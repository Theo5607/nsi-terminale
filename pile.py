class Pile():
    def __init__(self):
        self.L=[]
    
    def vide(self):
        return self.L==[]
        
    def depiler(self):
        assert not self.vide(), "Pile vide"
        return self.L.pop()
    
    def empiler(self, x):
        self.L.append(x)
        
    def taille(self):
        return len(self.L)
    
    def sommet(self):
        return self.L[-1]
    
    
def verification(chaine):
    pile1 = Pile()
    pile2 = Pile()
    for car in chaine:
        if car == '(':
            pile1.empiler(1)
        elif car == ')':
            if pile1.taille()==0:
                return False
            else:
                pile1.depiler()
                
        elif car == '[':
            pile2.empiler(1)
        elif car == ']':
            if pile2.taille()==0:
                return False
            else:
                pile2.depiler()
    if pile1.taille()==0 and pile2.taille()==0:
        return True
    else:
        return False
    
#print(verification('())(()'))


from copy import deepcopy

laby=[[0,1,0,0,0,0],[0,1,1,1,1,0],[0,1,0,1,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,0,1,0]]

lignes=len(laby)
colonnes=len(laby[1])

for ligne in laby:
    print(ligne)
    
def voisins(T,v):
    V=[]
    i,j=v[0],v[1]
    for a in(-1,1):
        if 0<=i+a<lignes:
            if T[i+a][j]==1:
                V.append((i+a,j))
            if 0<=j+a<colonnes:
                if T[i][j+a]==1:
                    V.append((i,j+a))
    return V

def parcours(labyrinthe, entree, sortie):
    T=labyrinthe
    p=Pile()
    v=entree
    labyrinthe[v[0]][v[1]]=-1
    recherche=True
    while recherche==True:
        vois=voisins(T,v)
        if len(vois)==0:
            p.depiler()
            if p.vide()==True:
                return False
            else:
                v=p.sommet()
        else:
            p.empiler(vois[0])
            v=vois[0]
            T[v[0]][v[1]]=-1
            if v==sortie:
                return p.L

print(parcours(laby, (0,1), (5,4)))