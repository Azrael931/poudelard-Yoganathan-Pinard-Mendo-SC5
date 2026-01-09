import random
from poudelard.univers.maison import actualiser_points_maison
from poudelard.utils.input_utils import load_fichier

def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    joueurs_liste = []
    i = 0
    while i < len(equipe_data["joueurs"]):
        joueurs_liste.append(equipe_data["joueurs"][i])
        i = i + 1

    if est_joueur and joueur is not None:
        nom_complet = joueur["prenom"] + " " + joueur["nom"]
        joueur_str = nom_complet + " (Attrapeur)"

        nouveaux = [joueur_str]
        i = 0
        while i < len(joueurs_liste):
            s = joueurs_liste[i]
            prefixe = s[0:len(nom_complet) + 1]
            if prefixe != nom_complet + " ":
                nouveaux.append(s)
            i = i + 1
        joueurs_liste = nouveaux

    return {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": joueurs_liste
    }

def tenter_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_marque = random.randint(1, 10)
    if proba_marque <= 6:
        if joueur_est_joueur:
            joueur_qui_marque = equipe_attaque["joueurs"][0]
        else:
            joueur_qui_marque = random.choice(equipe_attaque["joueurs"])
        equipe_attaque["score"] = equipe_attaque["score"] + 10
        equipe_attaque["a_marque"] = equipe_attaque["a_marque"] + 1
        print(joueur_qui_marque + " marque un but pour " + equipe_attaque["nom"] + " ! 10 points")
    else:
        equipe_defense["a_stoppe"] = equipe_defense["a_stoppe"] + 1
        print(equipe_defense["nom"] + " bloque l'attaque !")

def apparition_vifdor():
    proba_spawn = random.randint(1,6)
    if proba_spawn == 6 :
        return True
    else :
        return False

def attraper_vifdor(e1, e2):
    e_gagnante = random.choice([e1, e2])
    e_gagnante["score"] += 150
    e_gagnante["attrape_vifdor"] = True
    return e_gagnante

def afficher_score(e1, e2):
    print("Score actuel :")
    print(e1["nom"] + " : " + str(e1["score"]) + " points")
    print(e2["nom"] + " : " + str(e2["score"]) + " points")


def afficher_equipe(maison, equipe):
    print("Équipe de " + maison + " :")
    for joueur in equipe["joueurs"]:
        print("- " + joueur)

def match_quidditch(joueur, maisons):
    equipes_data = load_fichier("data/equipes_quidditch.json")

    maison_joueur = joueur["Maison"]

    maisons_possibles = []
    for nom in equipes_data:
        if nom != maison_joueur:
            maisons_possibles.append(nom)

    maison_adv = random.choice(maisons_possibles)

    equipe_joueur = creer_equipe(maison_joueur, equipes_data[maison_joueur], est_joueur=True, joueur=joueur)
    equipe_adv = creer_equipe(maison_adv, equipes_data[maison_adv])

    print("Match de Quidditch " + maison_joueur + " vs " + maison_adv + " !")
    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adv, equipe_adv)
    print("Tu joues pour " + maison_joueur + " en tant qu'Attrapeur")

    tour = 1
    while tour <= 20:
        print("----- Tour " + str(tour) + " -----")
        tenter_marque(equipe_joueur, equipe_adv, joueur_est_joueur=True)
        tenter_marque(equipe_adv, equipe_joueur, joueur_est_joueur=False)
        afficher_score(equipe_joueur, equipe_adv)

        if apparition_vifdor():
            gagnante_vif = attraper_vifdor(equipe_joueur, equipe_adv)
            print("Le Vif d'Or a été attrapé par " + gagnante_vif["nom"] + " ! 150 points")
            print("Fin du match !")
            break


        input("Appuyez sur Entrée pour continuer")
        tour = tour + 1

    print("Score final :")
    afficher_score(equipe_joueur, equipe_adv)

    if equipe_joueur["score"] > equipe_adv["score"]:
        print("Victoire de " + maison_joueur + " ! 500 points pour ta maison.")
        actualiser_points_maison(maisons, maison_joueur, 500)
    elif equipe_joueur["score"] < equipe_adv["score"]:
        print("Défaite... " + maison_adv + " remporte le match et gagne 500 points.")
        actualiser_points_maison(maisons, maison_adv, 500)
    else:
        print("Match nul, aucune maison ne gagne de points supplémentaires.")

def lancer_chapitre4_quidditch(joueur, maisons):
    print("Chapitre 4 : La grande finale de Quidditch !")
    input("Appuyez sur Entrée pour commencer le match...")
    match_quidditch(joueur, maisons)
    print("Fin du Chapitre 4 !")