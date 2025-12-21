from poudelard.utils.input_utils import demander_choix
from poudelard.chapitres.chapitre_1 import lancer_chapitre_1
from poudelard.chapitres.chapitre_2 import lancer_chapitre_2
from poudelard.chapitres.chapitre_3 import lancer_chapitre_3

def afficher_menu_principal():
    print("=== Bienvenue à Poudelard ===")
    print("Que souhaitez-vous faire ?")

def lancer_choix_menu():
    personnage = None
    maisons = {"Gryffondor": 0, "Serpentard": 0, "Poufsouffle": 0, "Serdaigle": 0}

    while True:
        afficher_menu_principal()
        options_menu = [
            "Lancer le Chapitre 1 – L’arrivée dans le monde magique.",
            "Quitter le jeu."
        ]
        choix = demander_choix("Votre choix :", options_menu)

        if choix == 1:
            personnage = lancer_chapitre_1()
            lancer_chapitre_2(personnage)
            lancer_chapitre_3(personnage, maisons)

        elif choix == 2:
            print("Merci d'avoir joué à Poudelard : à bientôt, jeune sorcier !")
            break

if __name__ == "__main__":
    lancer_choix_menu()
