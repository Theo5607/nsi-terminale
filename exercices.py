"""
Question 1:

Alain Térieur
Programmation : 12
Algorithmique : 10
Projet : 15
"""

class Eleve:

    matiere1="Programmation"
    matiere2="Algorithmique"
    matiere3="Projet"

    def __init__(self,Nom,Prenom,Date,Note1,Note2,Note3):
        self.nom=Nom
        self.prenom=Prenom
        self.date=Date
        self.note_mat1=Note1
        self.note_mat2=Note2
        self.note_mat3=Note3

    def moyenne(self):
        return ((self.note_mat1+self.note_mat2+self.note_mat3)/3)
        
eleve1=Eleve("Térieur","Alain","01/01/2000",12,10,15)
eleve2=Eleve("Onette","Camille","01/07/2004",7,14,11)
eleve3=Eleve("Oma","Modeste","01/11/2002",13,8,17)

def moyenne_gen(liste_eleves):
    dict_moy={"Programmation":0,"Algorithmique":0,"Projet":0}
    for el in liste_eleves:
        dict_moy["Programmation"]+=el.note_mat1
        dict_moy["Algorithmique"]+=el.note_mat2
        dict_moy["Projet"]+=el.note_mat3

    dict_moy["Programmation"]/=len(liste_eleves)
    dict_moy["Algorithmique"]/=len(liste_eleves)
    dict_moy["Projet"]/=len(liste_eleves)

    return dict_moy

print(moyenne_gen([eleve1,eleve2,eleve3]))
