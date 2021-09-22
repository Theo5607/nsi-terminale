import csv
reader = csv.DictReader(open("eleves.csv", "r"))
classe = []
for row in reader:
    classe.append(dict(row))

print(classe)

def moyenne(eleve):
    moy=(int(eleve["Programmation"])+int(eleve["Algorithmique"])+int(eleve["Projet"]))/3
    return moy
    
print("moyenne de ",classe[0]["Prenom"],classe[0]["Nom"]," : ",moyenne(classe[0]))
print("moyenne de ",classe[1]["Prenom"],classe[1]["Nom"]," : ",moyenne(classe[1]))
print("moyenne de ",classe[2]["Prenom"],classe[2]["Nom"]," : ",moyenne(classe[2]))