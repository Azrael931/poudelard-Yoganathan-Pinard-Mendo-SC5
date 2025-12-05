def actualiser_points_maison(maisons, nom_maison, points):
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle" : 0,
    }

    if nom_maison in maisons:
        maisons[nom_maison] += points
        print(f"La maison {nom_maison} a reçu {points} points.")
        print(f"Nouveau total : {maisons[nom_maison]}")
    else:
        print(f"Erreur : La maison '{nom_maison}' est introuvable.")

