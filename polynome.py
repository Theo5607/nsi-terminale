class Polynomial:
    """
    classe travaillant sur des polynome ex: 2x² + 5x + 6
    """
    def __init__(self, polylist=[]): #initialisation du polynome à travers une liste
        if not isinstance(polylist, list): # =on vérifie si c'est bien une liste
            raise ValueError("Ceci n'est pas une liste",str(polylist))
            
        self.lpolynome = polylist
        self.lpolynome = self.normalize()
    
    def __add__(self, other): #méthode permetant d'addtioner deux polynomes
        return Polynomial(addition(self.lpolynome,other.lpolynome)) #(passe à travers une fonction externe)
    
    def __sub__(self, other): #méthode permetant de soustraire deux polynomes
        return Polynomial(soustraction(self.lpolynome,other.lpolynome)) #(passe à travers une fonction externe)
    
    def __mul__(self, other): #méthode permetant de multiplier deux polynomes
        return Polynomial(multiply(self.lpolynome,other.lpolynome)) #(passe à travers une fonction externe)
        
    def __pow__(self, other): #méthode permettant de mettre un polynome a la puissance n
        return Polynomial(puissance(self.lpolynome,other.lpolynome)) #(passe à travers un fonction externe)
        
    def normalize(self): #méthode permettant de supprimer les 0 inutiles dans la liste lpolynome
        liste_0 = []
        for el in self.lpolynome:
            if el==0:
                liste_0.append(0)
            else:
                liste_0=[]
        
        new = [self.lpolynome[el] for el in range(len(self.lpolynome)-len(liste_0))]
        return new
    
    def degree(self): #méthode qui renvoie le degré du polynome en parametre
        return len(self.lpolynome)-1
        
    def equal(self, other): #méthode qui renvoie True si deux polynomes sont égaux
        self.normalize()
        other.normalize()
        
        if self.lpolynome==other.lpolynome:
            return True
        else:
            return False
            
    def derivative(self): #méthode qui renvoie la dérivée d'un polynome
        new=[0]*(len(self.lpolynome)-1)
        for i in range(0, len(self.lpolynome)-1):
            if i==0:
                new[i]=self.lpolynome[i+1]*1
            else:
                new[i]=self.lpolynome[i+1]*(i+1)
        self.lpolynome=new
        return self.lpolynome

        self.lpolynome=new
        return self.lpolynome

    def to_string(self): #méthode qui renvoie un polynome sous forme de chaine de caractères
        new_str=''
        for i in range(len(self.lpolynome),0,-1):
            if i-1==0:
                new_str+=str(self.lpolynome[i-1])
            elif i-1==1:
                new_str+=str(self.lpolynome[i-1])+'x'+'+'
            elif self.lpolynome[i-1]!=0:
                new_str+=str(self.lpolynome[i-1])+'x^'+str(i-1)+'+'
        return new_str
    
    def __repr__(self): #méthode qui appelle to_string()
        return self.to_string()
    
def addition(p1,p2): #méthode appelée dans la classe pour additionner deux polynomes
    if len(p1)>len(p2) : new = [0]*len(p1)
    else : new = [0]*len(p2)

    for i in range(len(p1)): new[i]+= p1[i]
    for i in range(len(p2)): new[i]+= p2[i]

    return new
    
def soustraction(p1,p2): #méthode appelée dans la classe pour soustraire deux polynomes
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
    
def multiply(p1,p2): #méthode appelée dans la classe pour multipliers deux polynomes
    new=[0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            new[i+j]+=p1[i]*p2[j]
    
    return new
    
def puissance(p1,n): #méthode appelée dans la classe pour mettre un polynome a la puissance n
    new=1
    for i in range(n):
        new*=p1

    return new
    
def mult_scal(p,c): #méthode pour multiplier un polynome par un scalaire c
    for i in range (len(p)):
        p[i]*=c
    return p

def horner(p,e): #méthode pour calculer l'image d'un polynome
    r=0
    i=0
    while i<=len(p)-1:
        r=r*e+p[len(p)-1-i]
        i+=1
    return r

def mult_monomial(p,c,i): #méthode pour multplier un polynome par un scalaire à la puissance i
    for i in range(i):
        p.insert(0,0)
    return mult_scal(p,c)
    
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

p10=Polynomial([3,2,1])
p11=Polynomial([1,4,2,4,3])
p12=p10*p11
print(p12.lpolynome)

p13=Polynomial([2,3,2,5])
p13.derivative()
print(p13.lpolynome)

p14=Polynomial([1,2,4,8])
print(p14)
"""
