def initialiser_personnage(nom, prenom, attributs): #initilisation du personnage

    joueur = {
        "nom": nom,
        "prenom": prenom,
        "argent": 100,
        "inventaire": [],
        "Sortilèges" : [],
        "attributs": attributs
    }
    return joueur

def afficher_personnage(joueur): #Affichage du personnage
    print("Profil du personnage : ")
    print(f"Nom : {joueur['nom']}")
    print(f"Prénom : {joueur['prenom']}")
    print(f"Argent : {joueur['argent']}")
    print("Inventaire : ")
    for objet in joueur["inventaire"]:
        print(f"- {objet}")
    print("Sortilèges :")
    for sortilege in joueur["Sortilèges"]:
        print(f"- {sortilege}")
    print("Attributs :")
    for attributs, valeur in joueur["attributs"].items():
        print(f"- {attributs} : {valeur}")

if __name__ == "__main__": #Test de la fonction afficher_personnage

    print("---Test Affichage du personnage---")
    attributs_test = {"courage": 8, "intelligence": 8, "loyaute": 8, "ambition" : 8,}
    joueur_test = initialiser_personnage("Harry", "Potter", attributs_test)
    afficher_personnage(joueur_test)



def modifier_argent(joueur, montant): #Modification de l'argent du joueur
    joueur["argent"] += montant
if __name__ == "__main__" : #Test de la fonction modifier_argent
    print("---Test Modification d'argent---")
print("tag for commit ")



def ajouter_objet_inventaire(joueur,cle, objet):
    joueur[cle].append(objet)
if __name__ == "__main__": #Test de la fonction ajouter_objet_inventaire
    print("---Test Ajout d'objet dans l'inventaire---")