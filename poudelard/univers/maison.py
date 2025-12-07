'''def actualiser_points_maison(maisons, nom_maison, points):
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0,
    }

    if nom_maison in maisons:
        maisons[nom_maison] += points
        print(f"La maison {nom_maison} a maintenant {maisons[nom_maison]} points.")
    else:
        print(f"Erreur : la maison '{nom_maison}' est introuvable.")'''


def afficher_maison_gagnante(maisons):
    max_point = 0
    maisons = {
        "Gryffondor": 5,
        "Serpentard": 8,
        "Poufsouffle": 7,
        "Serdaigle": 7,
    }
    for val in maisons.values():
        if max_point < val:
            max_point = val
    for k, v in maisons.items():
        if v == max_point:
         print("la maison ayant le score le plus élevé est :", k)



if __name__ == "__main__":
    maisons={}

    print(afficher_maison_gagnante(maisons))

