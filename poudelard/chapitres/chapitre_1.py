from poudelard.univers.personnage import *
from poudelard.utils.input_utils import *


def introduction():
    print("\n--- CHAPITRE 1 : L'arrivée dans le monde magique ---")
    print("Bienvenue dans le monde des sorciers !")
    input("Appuyez sur Entrée pour commencer l'aventure...")


def creer_personnage():
    nom = demander_texte("Veuillez choisir un nom : ")
    prenom = demander_texte("Veuillez choisir un prénom : ")
    print("Choisissez vos attributs (entre 1 et 10) :")
    attributs = {
        "courage": demander_nombre("Niveau de courage (1-10) :", 1, 10),
        "intelligence": demander_nombre("Niveau d'intelligence (1-10) :", 1, 10),
        "loyaute": demander_nombre("Niveau de loyauté (1-10) :", 1, 10),
        "ambition": demander_nombre("Niveau d'ambition (1-10) :", 1, 10)
    }
    joueur = initialiser_personnage(nom, prenom, attributs)
    afficher_personnage(joueur)
    return joueur


def recevoir_lettre():
    print("\nUne chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    print(
        "« Cher élève,\n Nous avons le plaisir de vous informer que vous avez été admis à l'école de sorcellerie de Poudlard ! »")
    print("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?")

    options_lettre = ["Oui, bien sûr !", "Non, je préfère rester avec l'oncle Vernon..."]
    choix = demander_choix("Votre choix :", options_lettre)

    if choix == 2:
        print("Vous déchirez la lettre. L'oncle Vernon pousse un cri de joie.")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit()


def rencontrer_hagrid(personnage):
    print(
        f"\nHagrid : 'Salut {personnage['prenom']} ! Je suis venu t'aider à faire tes achats sur le Chemin de Traverse.'")
    print("Voulez-vous suivre Hagrid ?")

    options_hagrid = ["Oui", "Non"]
    choix = demander_choix("Votre choix :", options_hagrid)

    if choix == 2:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui !")


def acheter_fournitures(personnage):
    inventaire_data = load_fichier("data/inventaire.json")

    if not inventaire_data:
        print("Erreur critique : Impossible de charger le catalogue.")
        return

    objets_obligatoires = {"Baguette magique", "Robe de sorcier", "Manuel de potions"}
    achats_faits = set()

    print("\n--- Bienvenue sur le Chemin de Traverse ! ---")

    while not objets_obligatoires.issubset(achats_faits):
        print(f"\nVous avez {personnage['argent']} galions.")
        manquants = objets_obligatoires - achats_faits
        print(f"Objets obligatoires restants : {', '.join(manquants)}")

        print("Catalogue :")
        for i, item in enumerate(inventaire_data, 1):
            print(f"{i}. {item['nom']} - {item['prix']} galions")

        choix = demander_nombre("Entrez le numéro de l'objet à acheter : ", 1, len(inventaire_data))
        objet_choisi = inventaire_data[choix - 1]

        if objet_choisi['nom'] in achats_faits:
            print("Vous avez déjà cet objet.")
            continue

        if personnage['argent'] >= objet_choisi['prix']:
            modifier_argent(personnage, -objet_choisi['prix'])
            ajouter_objet(personnage, "Inventaire", objet_choisi['nom'])
            achats_faits.add(objet_choisi['nom'])
            print(f"Vous avez acheté : {objet_choisi['nom']}")
        else:
            print("Fonds insuffisants !")
            if objet_choisi['nom'] in objets_obligatoires:
                print("C'est un objet obligatoire, vous ne pouvez pas aller à Poudlard sans lui.")
                print("Game Over.")
                exit()

    print("\nTous les objets obligatoires ont été achetés !")

    print("\nIl est temps de choisir votre animal de compagnie pour Poudlard !")
    print(f"Vous avez {personnage['argent']} galions.")

    animaux = [
        {"nom": "Chouette", "prix": 20},
        {"nom": "Chat", "prix": 15},
        {"nom": "Rat", "prix": 10},
        {"nom": "Crapaud", "prix": 5}
    ]

    for i, animal in enumerate(animaux, 1):
        print(f"{i}. {animal['nom']} ({animal['prix']} galions)")

    choix_animal = demander_nombre("Quel animal voulez-vous ? ", 1, 4)
    animal_choisi = animaux[choix_animal - 1]

    if personnage['argent'] >= animal_choisi['prix']:
        modifier_argent(personnage, -animal_choisi['prix'])
        ajouter_objet(personnage, "Inventaire", animal_choisi['nom'])
        print(f"Vous avez choisi : {animal_choisi['nom']}")
    else:
        print("Dommage, vous n'avez pas assez d'argent pour cet animal.")

    print("\nVoici votre inventaire final avant le départ :")
    afficher_personnage(personnage)


def lancer_chapitre_1():
    introduction()
    joueur = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(joueur)
    acheter_fournitures(joueur)
    print("\n<<< Fin du Chapitre 1 ! Votre aventure commence à Poudlard... >>>")
    return joueur


if __name__ == "__main__":
    lancer_chapitre_1()