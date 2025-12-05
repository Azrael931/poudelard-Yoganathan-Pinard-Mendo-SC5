def demander_texte(message):
    while  True:
        texte = input(message).strip()

        if len(texte) == 0:
            print("Veuillez entrer un texte non vide.")
        else:
            return texte

nom = demander_texte("Entrez le nom de votre personnage : ")
print("Bienvenue,", nom)

