from poudelard.utils.input_utils import demander_choix
from poudelard.chapitres.chapitre_1 import lancer_chapitre_1
joueur= lancer_chapitre_1()


def rencontrer_amis(joueur):
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
           joueur['loyaute']+=1
           print('Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !(loyauté:+1)' )
          else:
           joueur['ambition']+=1
           print('Ron est malheureux: — désolé pour le dérangement')
        if i==1:
          choix = demander_choix(message, options)
          if choix == 1:
            joueur['intelligence'] += 1
            print('Hermione est ravi: — ca nous fait un point en commun ')
          else:
            joueur['courage'] += 1
            print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour ! ")
        if i==2:
          choix = demander_choix(message, options)
          if choix == 1:
            joueur['ambition'] += 1
            print('Drago souris: - Enchanté je me nomme Drago Malfoy')
          elif choix == 2:
            joueur['loyaute'] += 1
            print("Drago fronce les sourcils, vexé. — Tu le regretteras ! ")
          elif choix == 3:
            joueur['courage'] += 1
            print('Drago est choqué: - comment oses tu!')
    print('Le train continue sa route. Le château de Poudlard se profile à l’horizon... \nTes choix semblent déjà en dire long sur ta personnalité ! ')
    print('Tes attributs mis à jour :', joueur)








rencontrer_amis(joueur)





