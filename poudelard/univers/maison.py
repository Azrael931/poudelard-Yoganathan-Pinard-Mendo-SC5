maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0,
    }

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


if __name__ == "__main__":
    print("\n--- Test 1 : Vainqueur unique ---")
    maisons_test_1 = {
        "Gryffondor": 150,
        "Serpentard": 120,
        "Poufsouffle": 50,
        "Serdaigle": 100
    }
    afficher_maison_gagnante(maisons_test_1)
    print("\n--- Test 2 : Égalité parfaite ---")
    maisons_test_2 = {
        "Gryffondor": 200,
        "Serpentard": 200,
        "Poufsouffle": 50,
        "Serdaigle": 100
    }
    afficher_maison_gagnante(maisons_test_2)

