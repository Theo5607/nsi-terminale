class Domino:
    
    def __init__(self,a,b):
        self.faceA=a
        self.faceB=b
        
    def affichePoints(self):
        print("La valeur de la face A est",self.faceA,"La valeur de la face B est",self.faceB)
        
    def total(self):
        return self.faceA+self.faceB
        
class CompteBancaire:
    
    def __init__(self,tit,argent=0):
        self.titulaire=tit
        self.solde=argent
        
    def depot(self,somme):
        self.solde+=somme
        
    def retrait(self,somme):
        self.solde-=somme
    
    def affiche(self):
        print("Bonjour, "+self.titulaire+", vous avez",self.solde,"dollars")