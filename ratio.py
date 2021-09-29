from math import *

def pgcd(x,y):
    return gcd(x,y)

# fichier ratio.py
class Rationnel:
    # création des instances
    def __init__(self,num,den=1):# par défaut le dénominateur vaut 1
        if den == 0:
            # on déclenche une exeption spécifique
            raise ZeroDivisionError("denominateur nul")
        else:
            self.num=num
            self.den=den
            self.normalise()
        
    # pour voir une fraction sur la console appelée par print
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
        
    #simplification des fractions
    def normalise(self):
        g = pgcd(abs(self.num),abs(self.den))
        self.num =self.num // g
        self.den =self.den //g
        if(self.num*self.den<0):
            if self.den<0:
                self.den=-self.den
                self.num=-self.num
        else:
            if self.den<0:
                self.den=-self.den
                self.num=-self.num
                
    def __add__(self, other): #addition
        n=self.num*other.den+other.num*self.den
        d=self.den*other.den
        return Rationnel(n,d)
    
    def __sub__(self, other): #soustraction
        n=self.num*other.den-other.num*self.den
        d=self.den*other.den
        return Rationnel(n,d)
        
    def __mul__(self, other): #multiplication
        n=self.num*other.num
        d=self.den*other.den
        return Rationnel(n,d)
    
    def __truediv__(self,other): #division
        n=self.num*other.den
        d=self.den*other.num
        return Rationnel(n,d)
        
def nombre_euler(n):
    e=Rationnel(0,1)
    for i in range(1,n+1):
        e+=Rationnel(1,factorial(i))
    
    return e

def nombre_pi(n):
    pi=Rationnel(0,1)
    for i in range(0,n+1):
        pi+=Rationnel((-1)**i,2*i+1)
    
    return Rationnel(4,1)*pi
