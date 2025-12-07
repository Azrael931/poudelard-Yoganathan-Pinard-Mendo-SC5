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


'''def afficher_maison_gagnante(maisons):
    g = maisons["Gryffondor"]
    s = maisons["Serpentard"]
    p = maisons["Poufsouffle"]
    e = maisons["Serdaigle"]

    if g > s and g > p and g > e:
        print("La maison gagnante est Gryffondor avec", g, "points.")

    elif s > g and s > p and s > e:
        print("La maison gagnante est Serpentard avec", s, "points.")

    elif p > g and p > s and p > e:
        print("La maison gagnante est Poufsouffle avec", p, "points.")

    elif e > g and e > s and e > p:
        print("La maison gagnante est Serdaigle avec", e, "points.")

    else:
        print("Il y a une égalité entre plusieurs maisons !")'''

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
if __name__ == "__main__":
    maisons={}

    print(afficher_maison_gagnante(maisons))

