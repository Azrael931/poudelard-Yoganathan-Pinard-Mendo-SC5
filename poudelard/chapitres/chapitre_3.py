import json
import random

with open("../data/sorts.json", "r", encoding="utf-8") as f:
    sorts = json.load(f)

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
print("Tu viens d'apprendre le sortilege : ", s1["nom"], "(Utilitaire)")
input("Appuie sur Entrée pour continuer")
s2 = random.choice(utilitaires)
print("Tu viens d'apprendre le sortilege : ", s2["nom"], "(Utilitaire)")
input("Appuie sur Entrée pour continuer")
s3 = random.choice(utilitaires)
print("Tu viens d'apprendre le sortilege : ", s3["nom"], "(Utilitaire)")
input("Appuie sur Entrée pour continuer")
s4 = random.choice(offensifs)
print("Tu viens d'apprendre le sortilege : ", s4["nom"], "(Offensif)")
input("Appuie sur Entrée pour continuer")
s5 = random.choice(defensifs)
print("Tu viens d'apprendre le sortilege : ", s5["nom"], "(Défensif)")

print("Tu as terminé ton apprentissage de base à Poudlard !\nVoici les sortilèges que tu maîtrises désormais :")

#( Travailler cette partie d''afficher la fonction des sort , je bloque )
print("-", s1["nom"], ":", s1["description"])
print("-", s2["nom"], ":", s2["description"])
print("-", s3["nom"], ":", s3["description"])
print("-", s4["nom"], ":", s4["description"])
print("-", s5["nom"], ":", s5["description"])





import json
import random

with open("../data/quiz_magie.json", "r", encoding="utf-8") as f:
    quiz_magie = json.load(f)


score = 0
Q1 = random.choice(quiz_magie)
juste = Q1[reponse]
rep = input(Q1)
if juste
    score = score + 25
    print("Bonne réponse ! tu gagnes +25 pints pour ta maison")
if
    print("Mauvaise reponse . La bonne réponse était",juste,)








'''ans = random.sample(sorts,4)
print('ans')
if ans == quiz_magie
score = score + 25'''