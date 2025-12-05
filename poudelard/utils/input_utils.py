def demander_texte(message):
    while  True:
        texte = input(message).strip()

        if len(texte) == 0:
            print("Veuillez entrer un texte non vide.")
        else:
            return texte

def demander_nombre(message, min_val=None, max_val=None):
    while True:
        texte = input(message + " ").strip()

        # Vérifier si la saisie est un nombre
        est_valide = True
        for c in texte:
            if c < '0' or c > '9':
                est_valide = False
                break

        if not est_valide:
            print("Veuillez entrer uniquement des chiffres.")
            continue

        # Conversion manuelle
        valeur = 0
        for c in texte:
            valeur = valeur * 10 + (ord(c) - ord('0'))

        # Vérification des bornes
        if min_val is not None and valeur < min_val:
            print(f"Veuillez entrer un nombre >= {min_val}.")
            continue

        if max_val is not None and valeur > max_val:
            print(f"Veuillez entrer un nombre <= {max_val}.")
            continue

        return valeur

