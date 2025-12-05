from poudelard.univers.personnage import initialiser_personnage
from poudelard.utils.input_utils import demander_texte
from poudelard.utils.input_utils import demander_nombre

def introduction():
    print("")

def creer_personnage():
    nom = demander_texte("Veuillez choisir un nom : ")
    prenom = demander_texte("Veuillez choisir un prénom : ")
    print("Choisissez vos attributs")
    attributs = {}
    attributs["courage"] = demander_nombre("Niveau de courage (1-10) :",1,10)
    attributs["ambition"] = demander_nombre("Niveau d'ambition (1-10) :",1,10)
    attributs["intelligence"] = demander_nombre("Niveau d'intelligence (1-10) :",1,10)
    attributs["loyauté"] = demander_nombre("Niveau de loyauté (1-10) :",1,10)
    return initialiser_personnage(nom, prenom, attributs)

if __name__ == "__main__":
    print("--- Début du test de création de personnage ---")
    perso = creer_personnage()
    print("Profil du personnage :")
    print(f"Nom : {perso['nom']}")
    print(f"Prenom : {perso['prenom']}")
    print(f"Argent : {perso['argent']}")
    print(f"Inventaire : {perso['inventaire']}")
    print("Attributs :")
    for attributs, valeur in perso["attributs"].items():
        print(f"- {attributs} : {valeur}")
    print("Sortilèges :")
    for sortilege in perso["Sortilèges"]:
        print(f"- {sortilege}")
    print("\n--- Résultat du test ---")
    print("Personnage créé avec succès !")


