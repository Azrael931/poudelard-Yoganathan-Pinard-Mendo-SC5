from poudelard.utils.input_utils import demander_choix


maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0,
    }
question_text=str()

def actualiser_points_maison(maisons, nom_maison, points):
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
        print(f"Les maisons gagnantes sont : {liste_gagnantes} avec {max_point} points")

def repartition_maison(joueur, questions):
    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    attributs = joueur['attributs']


    courage = attributs["courage"] if "courage" in attributs else 0
    ambition = attributs["ambition"] if "ambition" in attributs else 0
    loyaute = attributs["loyauté"] if "loyauté" in attributs else 0
    intelligence = attributs["intelligence"] if "intelligence" in attributs else 0

    scores["Gryffondor"] += courage * 2
    scores["Serpentard"] += ambition * 2
    scores["Poufsouffle"] += loyaute * 2
    scores["Serdaigle"] += intelligence * 2


    for texte, options, maisons_associees in questions:
        print(texte)

        reponse = demander_choix("Ton choix :", options)

        indice = reponse - 1
        
        if 0 <= indice < len(maisons_associees):
            maison = maisons_associees[indice]
            scores[maison] += 3
        else:
            print("Erreur de choix.")


    print("Résumé des scores :")
    for maison, score in scores.items():
        print(f"{maison} : {score} points")


    meilleure_maison = None
    meilleur_score = -1
    for maison, score in scores.items():
        if score > meilleur_score:
            meilleur_score = score
            meilleure_maison = maison

    return meilleure_maison


