from poudelard.chapitres.chapitre_1 import creer_personnage
from poudelard.univers.personnage import initialiser_personnage

maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0,
    }
question_text=str()

'''def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] += points
        print(f"La maison {nom_maison} a maintenant {maisons[nom_maison]} points.")
    else:
        print(f"Erreur : la maison '{nom_maison}' est introuvable.")

def afficher_maison_gagnante(maisons):
    max_point = 0
    for points in maisons.values():
        if points > max_point:
            max_point = points
    maisons_gagnantes = []
    for nom_maison, points in maisons.items():
        if points == max_point:
            maisons_gagnantes.append(nom_maison)
    if len(maisons_gagnantes) == 1:
        print(f"La maison gagnante est {maisons_gagnantes[0]} avec {max_point} points")
    else :
        liste_gagnantes = ", ".join(maisons_gagnantes)
        print(f"Les maisons gagnantes sont : {liste_gagnantes} avec {max_point} points")'''

def repartition_maison(joueur, questions):
    joueur =
    L = ["courir", "mourir", "applaudir"]
    questions = (question_text, L, maisons)
    print(questions[0])
    print(questions[1])
    i = int(input("faites un choix ?"))
    print(L[i])
    if i == 1:
        joueur["courage"] += 1
    print(joueur)



if __name__ == "__main__":
    joueur=
    joueur="michel"
    question_text="veux tu mourir?"
    L=["courir", "mourir", "applaudir"]
    questions=(question_text,L,maisons)
repartition_maison(joueur,questions)

