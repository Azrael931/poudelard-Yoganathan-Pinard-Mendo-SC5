import random
from poudelard.utils.input_utils import load_fichier
from poudelard.univers.maison import actualiser_points_maison, afficher_maison_gagnante
from poudelard.univers.personnage import afficher_personnage


def apprendre_sorts(personnage, chemin_fichier="data/sorts.json"):
    sorts = load_fichier(chemin_fichier)

    utilitaires = []
    offensifs = []
    defensifs = []

    for sort in sorts:
        if sort["type"] == "Utilitaire":
            utilitaires.append(sort)
        elif sort["type"] == "Offensif":
            offensifs.append(sort)
        elif sort["type"] == "Défensif":
            defensifs.append(sort)

    print("Tu commences tes cours de magie")

    s1 = random.choice(utilitaires)
    print("Tu viens d'apprendre le sortilege :", s1["nom"], "(Utilitaire)")
    input("Appuie sur Entrée pour continuer")
    utilitaires.remove(s1)

    s2 = random.choice(utilitaires)
    print("Tu viens d'apprendre le sortilege :", s2["nom"], "(Utilitaire)")
    input("Appuie sur Entrée pour continuer")
    utilitaires.remove(s2)

    s3 = random.choice(utilitaires)
    print("Tu viens d'apprendre le sortilege :", s3["nom"], "(Utilitaire)")
    input("Appuie sur Entrée pour continuer")
    utilitaires.remove(s3)

    s4 = random.choice(offensifs)
    print("Tu viens d'apprendre le sortilege :", s4["nom"], "(Offensif)")
    input("Appuie sur Entrée pour continuer")

    s5 = random.choice(defensifs)
    print("Tu viens d'apprendre le sortilege :", s5["nom"], "(Défensif)")

    # Ajout des sorts au personnage
    # On ajoute les noms des sorts pour que l'affichage soit propre
    personnage["Sortilèges"].append(s1["nom"])
    personnage["Sortilèges"].append(s2["nom"])
    personnage["Sortilèges"].append(s3["nom"])
    personnage["Sortilèges"].append(s4["nom"])
    personnage["Sortilèges"].append(s5["nom"])

    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")

    print("-", s1["nom"], ":", s1["description"])
    print("-", s2["nom"], ":", s2["description"])
    print("-", s3["nom"], ":", s3["description"])
    print("-", s4["nom"], ":", s4["description"])
    print("-", s5["nom"], ":", s5["description"])


def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):
    quiz_magie = load_fichier(chemin_fichier)

    if not quiz_magie:
        print("Aucune question disponible pour le quiz.")
        return 0

    score = 0

    selection = []
    nombre_questions_voulues = 4
    max_disponible = len(quiz_magie)
    cible = min(nombre_questions_voulues, max_disponible)

    while len(selection) < cible:
        q = random.choice(quiz_magie)
        if q not in selection:
            selection.append(q)

    for q in selection:
        juste = q.get("reponse", "")
        rep = input(q.get("question", "Question : ") + " ").strip().lower()
        juste1 = juste.strip().lower()

        if rep == juste1:
            score += 25
            print("Bonne réponse ! Tu gagnes +25 points pour ta maison")
        else:
            print("Mauvaise réponse. La bonne réponse était", juste)

    print("Ton score est de :", score)

    joueur["score"] = joueur.get("score", 0) + score
    print(f"Le score du joueur (total) est maintenant : {joueur['score']}")

    return score

def lancer_chapitre_3(personnage, maisons):
    apprendre_sorts(personnage)

    input("\nAppuie sur Entrée pour passer au quiz magique...")

    points_gagnes = quiz_magie(personnage)

    maison_joueur = personnage.get("Maison")
    if maison_joueur is None:
        print("Erreur : le personnage n'a pas de maison.")
        return

    actualiser_points_maison(maisons, maison_joueur, points_gagnes)

    print(f"\nTu gagnes {points_gagnes} points pour {maison_joueur} !")
    afficher_maison_gagnante(maisons)
    afficher_personnage(personnage)
