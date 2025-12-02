def demander_nom():
    nom=str(input("Etrer le nom de votre personnage :"))
    prénom=str(input("Etrer le prénom de votre personnage :"))
    message='welcome to Poudlard',nom+' '+prénom
    return message
print(demander_nom())


def demander_texte():
