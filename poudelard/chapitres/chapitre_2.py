from poudelard.univers.maison import repartition_maison
from poudelard.utils.input_utils import demander_choix, load_fichier
#création d'un joueur test dans un premier temps
joueur = {
    "nom": "Test",
    "prenom": "Joueur",
    "argent": 100,
    "inventaire": [],
    "Sortilèges": [],
    "attributs": {
        "courage": 5,
        "intelligence": 5,
        "loyauté": 5,
        "ambition": 5
    }
}
def rencontrer_amis(joueur):
    print("--- Début du test Chapitre 2 ---")
    for i in range(3):
        if i==0:
            options=[ "Bien sûr, assieds-toi !" , "Désolé, je préfère voyager seul."]
            message = "que repondez vous ?:\n"
        elif i==1:
            options=[ "Oui, j’adore apprendre de nouvelles choses ! ","Euh… non, je préfère les aventures aux bouquins."]
            message = "que repondez vous ?:\n"
        elif i==2:
            options=[". Je lui serre la main poliment.","Je l’ignore complètement.","Je lui réponds avec arrogance. "]
            message = "comment réagissez vous ?:\n"

        list_narrateur=["Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord... Un garçon roux entre dans votre compartiment, l’air amical.\n","Une fille entre ensuite, portant déjà une pile de livres.\n","Puis un garçon blond entre avec un air arrogant.\n"]
        list_phrase=["-Salut ! Moi c’est Ron Weasley.Tu veux bien qu’on s’assoie ensemble ? ","-Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?","-Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas"]
        print(list_narrateur[i],list_phrase[i])
        
        if i==0:
          choix=demander_choix(message, options)
          if choix == 1:
           joueur['attributs']['loyauté']+=1
           print('Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !(loyauté:+1)' )
          else:
           joueur['attributs']['ambition']+=1
           print('Ron est malheureux: — désolé pour le dérangement(ambition+1)')
        if i==1:
          choix = demander_choix(message, options)
          if choix == 1:
            joueur['attributs']['intelligence'] += 1
            print('Hermione est ravi: — ca nous fait un point en commun(intelligence+1)!')
          else:
            joueur['attributs']['courage'] += 1
            print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour ! (courage+1)")
        if i==2:
          choix = demander_choix(message, options)
          if choix == 1:
            joueur['attributs']['ambition'] += 1
            print('Drago souris: - Enchanté je me nomme Drago Malfoy(ambition+1)')
          elif choix == 2:
            joueur['attributs']['loyauté'] += 1
            print("Drago fronce les sourcils, vexé. — Tu le regretteras !(loyauté+1) ")
          elif choix == 3:
            joueur['attributs']['courage'] += 1
            print('Drago est choqué: - comment oses tu!?(courage+1)')
            
    print('Le train continue sa route. Le château de Poudlard se profile à l’horizon... \nTes choix semblent déjà en dire long sur ta personnalité ! ')
    print('Tes attributs mis à jour :', joueur['attributs'])
    return joueur


def mot_de_bienvenue():
    input("À l’entrée du Grand Hall, le directeur s’avance vers les nouveaux arrivants,\n son regard pétillant derrière ses lunettes en demi-lune.\n(cliquez sur entrée)")
    input("-Bienvenue, mon ami. Que ta curiosité soit ta plus grande magie, \net que chaque pas dans ce lieu t’ouvre un peu plus les portes de l’imaginaire.\n(cliquez sur entrée)\n" )


def ceremonie_repartition(joueur):
    input(" Les élèves s’avancèrent vers le tabouret, le Choixpeau prêt à révéler leur maison.\n La salle retenait son souffle.\n(cliquez sur entrée) ")
    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherchede l’aide", "Je reste calme et j’observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
             ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie","Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]
    maison_attribuee = repartition_maison(joueur, questions)
    print(f"La maison choisie est : {maison_attribuee}")
    return maison_attribuee


def installation_maison_commune(joueur, maison_attribuee):
    data_maisons = load_fichier("../data/maisons.json")

    info_maison = data_maisons[maison_attribuee]

    print(f"\n- Bienvenue à {maison_attribuee} {info_maison['emoji']} -")
    print(info_maison['description'])
    print(info_maison['message_installation'])

    print("\nBonus de maison appliqués :")
    for attribut, bonus in info_maison['bonus_attributs'].items():
        cle_attribut = attribut
        if attribut == "loyauté":
            cle_attribut = "loyaute"

        if cle_attribut in joueur['attributs']:
            joueur['attributs'][cle_attribut] += bonus
            print(f"- {attribut.capitalize()} : +{bonus}")

    print("\nVos attributs actuels :")
    for attr, val in joueur['attributs'].items():
        print(f"{attr.capitalize()} : {val}")

def lancer_chapitre_2():
    rencontrer_amis(joueur)
    mot_de_bienvenue()
    maison_attribuee=ceremonie_repartition(joueur)
    installation_maison_commune(joueur,maison_attribuee)
    print("\n- Fin du Chapitre 2 -\n Que vous attend dans cette nouvelle maison? A suivre...")

lancer_chapitre_2()




    



