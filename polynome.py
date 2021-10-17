class Polynomial:
    """
    classe travaillant sur des polynomes ex: 2x² + 5x + 6
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

    def __pow__(self, other): #méthode permettant de mettre un polynome à la puissance n
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

    def horner(self,other): #méthode permentant de donner l'image de e par fonction representee par un polynome
        return horner(self.lpolynome,other)

    def mult_monomial(self,c,i): #méthode pour multplier un polynome par un polynome monomial represente par c son multiplicateur et i sa puissance donc de forme cX**i
        return mult_monomial(self.lpolynome,c,i)

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

def addition(p1,p2):
    """
    -fonction appelée dans la classe pour additionner deux polynomes
    -prend en arguments p1 et p2 deux polynomes sous formes de listes
    -retourne un polynome sous forme de liste
    """
    if len(p1)>len(p2) : new = [0]*len(p1)
    else : new = [0]*len(p2)

    for i in range(len(p1)): new[i]+= p1[i]
    for i in range(len(p2)): new[i]+= p2[i]

    return new

def soustraction(p1,p2):
    """
    -fonction appelée dans la classe pour soustraire deux polynomes
    -prend en arguments p1 et p2 deux polynomes sous formes de listes
    -retourne un polynome sous forme de liste
    """
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
    """
    -fonction appelée dans la classe pour multipliers deux polynomes
    -prend en argument deux polynomes sous formes de listes
    -retourne le produit des deux
    """
    new=[0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            new[i+j]+=p1[i]*p2[j]

    return new

def puissance(p1,n):
    """
    -fonction appelée dans la classe pour mettre un polynome à la puissance n
    -prend en arguments p1 un polynome sous forme de liste et n la puissance à laquelle on veut le mettre
    -retourne un nouveau polynome à la puissance demandée
    """
    new=1
    for i in range(n):
        new*=p1

    return new

def mult_scal(p,c):
    """
    -fonction pour multiplier un polynome sous forme de liste par un scalaire
    -prend en arguments p un polynome et c un entier
    -retourne un nouveau polynome égal à p mutliplié par c
    """
    tmp_scal=list(p)
    for i in range (len(tmp_scal)):
        tmp_scal[i]*=c
    return tmp_scal

def horner(p,e):
    """
    -fonction permétant de donner l'image de e par fonction représentée par un polynome
    -prend en arguments p un polynome sous forme de liste et e un entier
    -retourne un entier image de e par p
    """
    r=0
    i=0
    while i<=len(p)-1:
        r=r*e+p[len(p)-1-i]
        i+=1
    return r

def mult_monomial(p,c,i):
    """
    -fonction pour multplier un polynome par un polynome monomial représenté par c son multiplicateur et i sa puissance donc de forme cX**i
    -prend en arguments p un polynome sous forme de liste c et i des entiers
    """
    tmp_mono=list(p)
    for i in range(i):
        tmp_mono.insert(0,0)
    fin_mono=mult_scal(tmp_mono,c)
    return fin_mono


def mult(p1,p2):
    """
    -alternative à la fonction multiply qui utilise la multiplication monomiale
    -prend en argument deux polynomes sous formes de listes
    -retourne le produit des deux
    """
    tmp_mult=[]
    for i in range(len(p2)):
        tmp_mult=list(addition(tmp_mult,mult_monomial(p1,p2[i],i)))
    return tmp_mult


#------------------------------------------------------------------------------------------------------------------
#Tests dans le shell des differentes methodes

#Test de l'addition
p1=Polynomial([1,2,3])
p2=Polynomial([3,2,1])
p3=p1+p2
print("La somme des polynomes p1 et p2 est égale à:",p3.lpolynome)


#Test de la soustraction
p4=Polynomial([-2,5,0,-2,0,1])
p5=Polynomial([-4,0,3,0,1])
p6=p4-p5
print("La différence des polynomes p4 et p5 est égale à:",p6.lpolynome)


#Test du degre
p7=Polynomial([1,2,2,5])
print("Le degré de p7 est:",p7.degree())


#Test de la verfication de l'égalite
p8=Polynomial([1,6,4,8,0,0])
p9=Polynomial([1,6,4,8])
print("Le fait que p8 est égal à p8 est:",p8.equal(p9))

p10=Polynomial([7,90,45,7,99])
p11=Polynomial([1,8,58])
print("Le fait que p10 est égal à p11 est:",p10.equal(p11))


#Test de la transformation en vrai polynome
p12=Polynomial([1,4,0,5])
print("La forme écrite de p12 est:",p12.to_string())


#Test de la multiplication
p13=Polynomial([3,2,1])
p14=Polynomial([1,4,2,4,3])
p15=p13*p14
print("Le produit de p13 et p14 est égal à:",p15.lpolynome)


#Test de la derivation du polynome
p16=Polynomial([2,3,2,5])
p16.derivative()
print("La dérivée de p16 est:",p16.lpolynome)


#Test de l'affichage direct en vrai polynome
p17=Polynomial([1,2,4,8])
print("La forme écrite de p12 est:",p17)


#Test de la methode horner()
p18=Polynomial([8,3,5])
p18_3=p18.horner(3)
print("L'image de 3 par p18 est:",p18_3)


#Test de la methode mult_monomial()
p19=Polynomial([2,5,4,7])
p20=p19.mult_monomial(3,5)
print("Le produit de p19 par le monomial 3x^5 est égal à:", p20)


#Test de la multiplaction avec la fonction mult()
p21=list(p13.lpolynome) #[3,2,1]
p22=list(p14.lpolynome) #[1,4,2,4,3]
p23=mult(p21,p22)
print("Le produit de p21 et p22 est égal à:",p23)
