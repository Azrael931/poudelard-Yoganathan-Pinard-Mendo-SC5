def initialiser_personnage(prenom, nom, attributs):

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
    print(f"Inventaire : {joueur['inventaire']}")
    print("Sortilèges :")
    for sortilege in joueur["Sortilèges"]:
        print(f"- {sortilege}")
    print("Attributs :")
    for attributs, valeur in joueur["attributs"].items():
        print(f"- {attributs} : {valeur}")

if __name__ == "__main__":

    print("---Test Affichage du personnage---")
    attributs_test = {"courage": 7, "ambition": 8, "intelligence": 9, "loyauté" : 10,}
    joueur_test = initialiser_personnage("Harry", "Potter", attributs_test)
    afficher_personnage(joueur_test)



def modifier_argent(joueur, montant):
    joueur["argent"] += montant

def ajouter_objet_inventaire(joueur,cle, objet):
    joueur[cle].append(objet)
