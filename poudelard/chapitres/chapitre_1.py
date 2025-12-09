import json

from poudelard.univers.personnage import *
from poudelard.utils.input_utils import *

def introduction():
    print("")

def creer_personnage(): #Création d'un personnage
    nom = demander_texte("Veuillez choisir un nom : ")
    prenom = demander_texte("Veuillez choisir un prénom : ")
    print("Choisissez vos attributs :")
    attributs = {}
    attributs["courage"] = demander_nombre("Niveau de courage (1-10) :",1,10)
    attributs["intelligence"] = demander_nombre("Niveau d'intelligence (1-10) :",1,10)
    attributs["loyaute"] = demander_nombre("Niveau de loyauté (1-10) :",1,10)
    attributs["ambition"] = demander_nombre("Niveau de ambition (1-10) :",1,10)
    return initialiser_personnage(nom, prenom, attributs)

if __name__ == "__main__": #Test de la fonction creer_personnage
    joueur = creer_personnage()
    afficher_personnage(joueur)

def recevoir_lettre(): #Réception de la lettre pour Poudlard
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    print("«Cher, élève,\n Nous avons le plaisir de vous informer que vous avez été admis à l'école de sorcellerie de Poudlard !»\n Souhaitez-vous accepter cette invitation et partir pour Pourdlard ?")
    options_lettre = ["Oui, bien sûr !", "Non, je préfère rester avec l'oncle Vernon..."]
    reponses_lettre = demander_choix("Votre choix :", options_lettre)
    if reponses_lettre == 2:
        print("Vous avez vécu une vie de Moldu et vous êtes mort.")
        exit()


if __name__ == "__main__": #Test de la fonction recevoir_lettre
    recevoir_lettre()

def rencontrer_hagrid(personnage): #Rencontre avec Hagrid
    print(f"Hagrid : 'Salut {personnage['prenom']} ! Je suis venu t'aider à faire tes achats sur le Chemin de Traverse.'\n Voulez-vous suivre Hagrid ?")
    options_hagrid = ["Oui","Non"]
    reponses_hagrid = demander_choix("Votre choix",options_hagrid)
    if reponses_hagrid == 2:
        print("Hagrid vous attrape par les oreilles et vous entraîne quand même avec lui !")

if __name__ == "__main__": #Test de la fonction rencontrer_hagrid
    rencontrer_hagrid(joueur)

def acheter_fournitures(personnage) :
    json.load(poudelard.data.inventaire.json)
