def actualiser_points_maison(maisons, nom_maison, points):
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle" : 0,
    }

    if nom_maison in maisons:
        maisons[nom_maison] += points
        print(f"La maison {nom_maison} a maintenant {maisons[nom_maison]} points.")
    else:
        print(f"Erreur : la maison '{nom_maison}' est introuvable.")


'''if __name__ == "__main__":
    maisons = {
        "Gryffondor": 50,
        "Serpentard": 30,
        "Poufsouffle": 20,
        "Serdaigle": 40
    }

    actualiser_points_maison(maisons, "Gryffondor", 10)
    actualiser_points_maison(maisons, "Serpentard", -5)
    actualiser_points_maison(maisons, "Poubelle", 15)

    print("État final :", maisons)'''

