import json

from poudelard.univers.personnage import *
from poudelard.utils.input_utils import *
import sys


def introduction():
    print("")

def creer_personnage(): #Création d'un personnage
    nom = demander_texte("Veuillez choisir un nom : ")
    prenom = demander_texte("Veuillez choisir un prénom : ")
    print("Choisissez vos attributs :")
    attributs = {
        "courage": demander_nombre("Niveau de courage (1-10) :", 1, 10),
        "intelligence": demander_nombre("Niveau d'intelligence (1-10) :", 1, 10),
        "loyaute": demander_nombre("Niveau de loyauté (1-10) :", 1, 10),
        "ambition": demander_nombre("Niveau de ambition (1-10) :", 1, 10)
    }
    return initialiser_personnage(nom, prenom, attributs)

def recevoir_lettre(): #Réception de la lettre pour Poudlard
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    print("«Cher, élève,\n Nous avons le plaisir de vous informer que vous avez été admis à l'école de sorcellerie de Poudlard !»\n Souhaitez-vous accepter cette invitation et partir pour Pourdlard ?")
    options_lettre = ["Oui, bien sûr !", "Non, je préfère rester avec l'oncle Vernon..."]
    reponses_lettre = demander_choix("Votre choix :", options_lettre)
    if reponses_lettre == 2:
        print("Vous avez vécu une vie de Moldu et vous êtes mort.")
        exit()

def rencontrer_hagrid(personnage): #Rencontre avec Hagrid
    print(f"Hagrid : 'Salut {personnage['prenom']} ! Je suis venu t'aider à faire tes achats sur le Chemin de Traverse.'\n Voulez-vous suivre Hagrid ?")
    options_hagrid = ["Oui","Non"]
    reponses_hagrid = demander_choix("Votre choix",options_hagrid)
    if reponses_hagrid == 2:
        print("Hagrid vous attrape par les oreilles et vous entraîne quand même avec lui !")

def acheter_fournitures(personnage):
    inventaire_data = load_fichier("poudelard/data/inventaire.json")
    if not inventaire_data:
        return

    objets_obligatoires = {"Baguette magique", "Robe de sorcier", "Manuel de potions"}
    achats_faits = set()

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
            ajouter_objet_inventaire(personnage, "Inventaire", objet_choisi['nom'])
            achats_faits.add(objet_choisi['nom'])
            print(f"Vous avez acheté : {objet_choisi['nom']}")
        else:
            print("Fonds insuffisants !")
            if objet_choisi['nom'] in objets_obligatoires:
                print("C'est un objet obligatoire, vous avez perdu la partie.")
                sys.exit(0)

    # Choix animal
    print("\nChoisissez un animal de compagnie :")
    animaux = ["Chouette (20)", "Chat (15)", "Rat (10)", "Crapaud (5)"]
    for i, animal in enumerate(animaux, 1):
        print(f"{i}. {animal}")
    prix_animaux = [20, 15, 10, 5]
    noms_animaux = ["Chouette", "Chat", "Rat", "Crapaud"]

    choix_animal = demander_nombre("Votre choix (1-4) : ", 1, 4)
    prix = prix_animaux[choix_animal - 1]
    nom = noms_animaux[choix_animal - 1]

    if personnage['argent'] >= prix:
        modifier_argent(personnage, -prix)
        ajouter_objet_inventaire(personnage, "Inventaire", nom)
    else:
        print("Pas assez d'argent pour l'animal. Tant pis !")
    print("tag for commit ")


if __name__ == "__main__":
    joueur = creer_personnage()
    afficher_personnage(joueur)
    recevoir_lettre()
    rencontrer_hagrid(joueur)
    acheter_fournitures(joueur)
