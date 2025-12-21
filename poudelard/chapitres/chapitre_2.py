from poudelard.chapitres.chapitre_1 import creer_personnage
from poudelard.utils.input_utils import demander_choix

def rencontrer_amis(joueur):
    for i in range(3):
        if i==0:
            options=[ "Bien sûr, assieds-toi !" , "Désolé, je préfère voyager seul."]
            message = "que repondez vous ?:"
        elif i==1:
            options=[ "Oui, j’adore apprendre de nouvelles choses ! ","Euh… non, je préfère les aventures aux bouquins."]
            message = "que repondez vous ?:"
        elif i==2:
            options=[". Je lui serre la main poliment.","Je l’ignore complètement.","Je lui réponds avec arrogance. "]
            message = "comment réagissez vous ?:"

        list_narrateur=["Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord... Un garçon roux entre dans votre compartiment, l’air amical.\n","Une fille entre ensuite, portant déjà une pile de livres.\n","Puis un garçon blond entre avec un air arrogant.\n"]
        list_phrase=["-Salut ! Moi c’est Ron Weasley.Tu veux bien qu’on s’assoie ensemble ? ","-Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?","-Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas"]
        print(list_narrateur[i],list_phrase[i])
        if i==0:
          choix=demander_choix(message, options)
          if choix == 1:
           joueur['loyaute']+=1
           print('Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !(loyauté:+1)' )
          else:
           joueur['ambition']+=1
           print(joueur)
        if i==1:
          choix = demander_choix(message, options)
          if choix == 1:
            joueur['intelligence'] += 1
            print(joueur)
          else:
            joueur['courage'] += 1
            print(joueur)
        if i==2:
          choix = demander_choix(message, options)
          if choix == 1:
            joueur['ambition'] += 1
            print(joueur)
          elif choix == 2:
            joueur['loyaute'] += 1
            print(joueur)
          elif choix == 3:
            joueur['courage'] += 1
            print(joueur)
    return joueur




i=0

options=[ "Bien sûr, assieds-toi !" , "Désolé, je préfère voyager seul."]
joueur={'loyaute': 0, 'courage': 0, 'intelligence': 0, 'ambition': 0}
rencontrer_amis(joueur)





