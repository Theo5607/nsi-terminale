from faker import Faker
import timeit

fake = Faker("fr_FR")

def genere_carnet1(n):
    """Renvoie une liste de n contacts aléatoires"""
    L_contacts=[]
    for i in range(n+1):
        contact={"nom": fake.name(), "tel": fake.phone_number(), "rue": fake.street_address(), "code": fake.postcode(), "ville": fake.city(), "naissance": "", "passwd": fake.password()}
        L_contacts.append(contact)
    return L_contacts

def est_present(nom, carnet):
    """Teste si nom est présent dans le carnet d'adresse"""
    for el in carnet:
        if el["nom"]==nom:
            return True
    return False
    
def genere_carnet2(n):
    D_contacts={}
    for i in range(n+1):
        name=fake.name()
        D_contacts[name]={"tel": fake.phone_number(), "rue": fake.street_address(), "code": fake.postcode(), "ville": fake.city(), "naissance": "", "passwd": fake.password()}
    return D_contacts
    
debut=timeit.default_timer()
n=10000
carnet1 = genere_carnet1(n)
nom = carnet1[-1]["nom"]
assert est_present(nom, carnet1)
assert not est_present("Lecluse Olivier", carnet1)
fin=timeit.default_timer()

print("Le parcours du carnet de",n,"adresses sous forme de liste prend",fin-debut,"secondes.")

debut=timeit.default_timer()
n=10000000
carnet2 = genere_carnet2(n)
nom = list(carnet2.keys())[-1]
fin=timeit.default_timer()

print("Le parcours du carnet de",n,"adresses sous forme de dictionnaire prend",fin-debut,"secondes.")