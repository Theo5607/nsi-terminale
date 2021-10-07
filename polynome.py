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
    
    def __mul__(self, other):
        return Polynomial(multiply(self.lpolynome,other.lpolynome))
        
    def __pow__(self, other):
        return Polynomial(puissance(self.lpolynome,other.lpolynome))
        
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
        
    def equal(self, other):
        self.normalize()
        other.normalize()
        
        if self.lpolynome==other.lpolynome:
            return True
        else:
            return False
            
    def to_string(self):
        new_str=''
        for i in range(len(self.lpolynome),0,-1):
            if i-1==0:
                new_str+=str(self.lpolynome[i-1])
            elif self.lpolynome[i-1]!=0:
                new_str+=str(self.lpolynome[i-1])+'x^'+str(i-1)+'+'
        return new_str
    
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
    
def multiply(p1,p2):
    new=[0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            new[i+j]+=p1[i]*p2[j]
    
    return new
    
def puissance(p1,n):
    new=1
    for i in range(n):
        new*=p1

    return new
"""
p1=Polynomial([-2,5,0,-2,0,1])
p2=Polynomial([-4,0,3,0,1])
p3=p1-p2
print(p3.lpolynome)

p4=Polynomial([0,0,0,2,4,0,0,0])
print(p4.lpolynome)

p5=Polynomial([1,2,2,5])
print(p5.degree())

p6=Polynomial([1,6,4,8,0,0])
p7=Polynomial([1,6,4,8])
print(p6.equal(p7))


p9=Polynomial([1,4,0,5])
print(p9.to_string())

p10=Polynomial([1,4,2])
p11=Polynomial([3,2,1])
p12=p10*p11
print(p12.lpolynome)
"""
