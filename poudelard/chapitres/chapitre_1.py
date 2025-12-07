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
    perso = creer_personnage()
    afficher_personnage(perso)

def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    print("«Cher, élève,\n Nous avons le plaisir de vous informer que vous avez été admis à l'école de sorcellerie de Poudlard !»\n Souhaitez-vous accepter cette invitation et partir pour Pourdlard ?")
    choix = ["Oui, bien sûr !", "Non, je préfère rester avec l'oncle Vernon..."]
    demander_choix("Votre choix :", choix)
    if choix == 2:
        exit()

if __name__ == "__main__": #Test de la fonction recevoir_lettre
    recevoir_lettre()

def rencontrer_hagrid(personnage):
    print(f"Hagrid : 'Salut {personnage['prenom']} ! Je suis venu t'aider à faire tes achats sur le Chemin de Traverse.'\n Voulez-vous suivre Hagrid ?")
    choix = ["Oui","Non"]
    demander_choix("Votre choix",choix)

if __name__ == "__main__":
    rencontrer_hagrid(perso)