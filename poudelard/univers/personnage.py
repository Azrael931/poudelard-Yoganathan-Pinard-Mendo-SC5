from poudelard.utils.input_utils import demander_nom

def initialiser_personnage(prenom,nom,argent,ambition,courage,loyaute,intelligence):
    return {
        "prenom" : prenom,
        "nom" : nom,
        "argent" : argent,
        "inventaire" : [],
        "sortilèges" : [],
        "attributs" : {
            "ambition" : ambition,
            "courage" : courage,
            "intelligence" : intelligence,
            "loyauté" : loyaute,

        }

    }

def afficher_personnage(personnage):
    print(f"Profil du personnage :")
    print(f"Nom : {personnage['nom']}")
    print(f"Prénom : {personnage['prenom']}")
    print(f"Argent : {personnage['argent']}")
    print(f"Inventaire : {personnage['inventaire']}")
    print(f"Sortilèges : {personnage['sortilèges']}")
    print(f"Attributs :")
    print(f"    -Ambition : {personnage['attributs']['ambition']}")
    print(f"    -Courage : {personnage['attributs']['courage']}")
    print(f"    -Intelligence : {personnage['attributs']['intelligence']}")
    print(f"    -Loyauté : {personnage['attributs']['loyauté']}")

if __name__ == "__main__":
    nom, prenom = demander_nom()
    joueur = initialiser_personnage(prenom, nom, 100, 5, 5, 5, 5)
    afficher_personnage(joueur)