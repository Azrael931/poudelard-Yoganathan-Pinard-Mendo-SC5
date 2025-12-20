import json

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

        est_valide = True
        est_negatif = False

        if texte == "":
            est_valide = False

        else:
            if texte[0] == "-":
                est_negatif = True
                if len(texte) == 1:
                    est_valide = False
                else:
                    a_verifier = texte[1:]
            else:
                a_verifier = texte

            if est_valide:
                for c in a_verifier:
                    if c < "0" or c > "9":
                        est_valide = False
                        break

        if not est_valide:
            print("Veuillez entrer uniquement des chiffres.")
            continue

        valeur = 0
        for c in a_verifier:
            valeur = valeur * 10 + (ord(c) - ord("0"))

        if est_negatif:
            valeur = -valeur

        if min_val is not None and valeur < min_val:
            print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            continue

        if max_val is not None and valeur > max_val:
            print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            continue

        return valeur


def demander_choix(message, options):
    while True :

        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        choix = demander_nombre(message, 1, len(options))
        return choix


if __name__ == "__main__":
    mes_options = ["Fleur","Gâteau","Viande"]
    print("---TEST DEMANDER CHOIX---")
    resultat = demander_choix("Tu préfères quoi entre : ", mes_options)
    print(f"Tu préfères {mes_options[resultat - 1]}")

def load_fichier(chemin_fichier):
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            return json.load(f)
