from poudelard.chapitres.chapitre_1 import creer_personnage


def rencontrer_amis(joueur):
    print("Salut ! Moi c’est Ron Weasley.Tu veux bien qu’on s’assoie ensemble ? ")
    rep = {"1": " Bien sûr, assieds-toi ! ", "2": "Désolé, je préfère voyager seul. "}
    print(f"Faites un choix: {rep['1']},{rep['2']}")
    choix = input("Votre choix (1 ou 2): ")
    if choix == '1':
        print("Super!")
        joueur['loyaute']+=1
        print(joueur)
    else:
        print('Dommage')
        joueur['ambition']+=1
        print(joueur)
    return joueur



if __name__ == "__main__":
    joueur = {'courage': 0, 'intelligence': 0, 'loyaute': 0, 'ambition': 0}
    rencontrer_amis(joueur)


