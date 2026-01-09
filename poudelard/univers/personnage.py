def initialiser_personnage(nom, prenom, attributs):

    joueur = {
        "nom": nom,
        "prenom": prenom,
        "argent": 100,
        "inventaire": [],
        "Sortilèges" : [],
        "attributs": attributs
    }
    return joueur

def afficher_personnage(joueur):
    print("Profil du personnage : ")
    print(f"Nom : {joueur['nom']}")
    print(f"Prénom : {joueur['prenom']}")
    print(f"Argent : {joueur['argent']}")
    print("Inventaire : ")
    for objet in joueur.get("inventaire", []):
        print(f"- {objet}")
    print("Sortilèges :")
    for sortilege in joueur.get("Sortilèges", []):
        print(f"- {sortilege}")
    print("Attributs :")
    for attributs, valeur in joueur.get("attributs", {}).items():
        print(f"- {attributs} : {valeur}")



def modifier_argent(joueur, montant):
    joueur["argent"] += montant


def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)


if __name__ == "__main__":
    print("---Test Affichage du personnage---")
    attributs_test = {"courage": 8, "intelligence": 8, "loyaute": 8, "ambition" : 8,}
    joueur_test = initialiser_personnage("Harry", "Potter", attributs_test)
    afficher_personnage(joueur_test)
    print("---Test Modification d'argent---")
    modifier_argent(joueur_test, -10)
    afficher_personnage(joueur_test)
    print("---Test Ajout d'objet dans l'inventaire---")
    ajouter_objet(joueur_test, "inventaire", "Baguette magique")
    afficher_personnage(joueur_test)
