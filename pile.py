class Pile():
    def __init__(self):
        self.L=[]
    
    def vide(self):
        return p==[]
        
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
    
print(verification('())(()'))
