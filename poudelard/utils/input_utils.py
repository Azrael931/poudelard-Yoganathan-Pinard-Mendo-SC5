def demander_nom():
    nom = str(input("Entrer le nom de votre personnage : "))
    prenom = str(input("Entrer le prénom de votre personnage : "))
    message = 'Welcome to Poudlard ' + nom + ' ' + prenom
    print(message)
    return nom, prenom

