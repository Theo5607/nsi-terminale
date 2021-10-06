class Polynomial:
    def __init__(self, polylist=[]):
        if not isinstance(polylist, list):
            raise ValueError("Ceci n'est pas une liste",str(polylist))
            
        self.lpolynome = polylist
        self.lpolynome = self.normalize()
    
    def __add__(self, other):
        return Polynomial(addition(self.lpolynome,other.lpolynome))
    
    def __sub__(self, other):
        return Polynomial(soustraction(self.lpolynome,other.lpolynome))
        
    def normalize(self):
        liste_0 = []
        for el in self.lpolynome:
            if el==0:
                liste_0.append(0)
            else:
                liste_0=[]
        
        new = [self.lpolynome[el] for el in range(len(self.lpolynome)-len(liste_0))]
        return new
    
    def degree(self):
        return len(self.lpolynome)-1
    
def addition(p1,p2):
    if len(p1)>len(p2) : new = [0]*len(p1)
    else : new = [0]*len(p2)

    for i in range(len(p1)): new[i]+= p1[i]
    for i in range(len(p2)): new[i]+= p2[i]

    return new
    
def soustraction(p1,p2):
    if len(p1)>len(p2) : 
        new = [0]*len(p1)
        for i in range(len(p1)-len(p2)):
            p2.append(0)
    else: 
        new = [0]*len(p2)
        for i in range(len(p1)-len(p2)):
            p2.append(0)

    for i in range(len(p1)): new[i]= p1[i]-p2[i]
    
    return new

p1=Polynomial([-2,5,0,-2,0,1])
p2=Polynomial([-4,0,3,0,1])
p3=p1-p2
print(p3.lpolynome)

p4=Polynomial([0,0,0,2,4,0,0,0])
print(p4.lpolynome)

p5=Polynomial([1,2,2,5])
print(p5.degree())
