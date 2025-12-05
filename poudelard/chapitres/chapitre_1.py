ambition = 8
courage = 8
intelligence = 81
argent = 100
print("Nous somme en été 1991, tu es seul chez toi (ca fait des années que tu vies seul). Tu decides de t'occupé cette apres midi ")
N = input("tu decides de lire un livre (1) ou de jouer a un jeu video (2) : ""\n")
if N == "1":
    print("un bruit sourd tape contre la vitre et te sort de ta lecture")
else :
    print("un bruit sourd tape contre la vitre et te derange pendant ta partie")
print("tu sors voir dehors ce qu'il se passe et tu vois un hibou avec une lettre")
M = int(input("Tu decide de jeter la lettre et retourner au ton occupation rapidement (1) ou tu decides de manger le hibou car tu as rien a manger ce soir et de jetter la lettre quand meme(2)""\n"))
if M == 1:
    ambition = ambition - 1
    print("Tu as rien a manger ce soir donc tu perd de l'ambition")
    print("Tu as donc perdu 1 d'ambition et maintenant tu passes a ", ambition, "d'ambition")
else:
    ambition = ambition + 1
    print(" grace a cette idée tu vas pouvoir manger ce soir , tu gagnes donc 1 d'ambition")
    print("Tu as donc gagner 1 d'ambition et maintenant tu passes a ",ambition,"d'ambition ""\n")

print("Tu vas a ton travail du soir, et en sortant de ton travail , un homme bardu mesurant au alentour de 3m te demande de le suivre")
O = int(input("tu decides de le suivre car tu est curieux (1) , Tu decides de t'enfuir car tu as peur (2) ou tu decides de te battre contre lui (3)""\n"))
if O == 1:
    courage = courage + 2
    print("tu gagnes +2 en courage, maintenant tu as ",courage," de courage ")
elif O == 2:
    courage = courage - 2
    print("Tu as peur et tu decides de fuir donc ton courage diminue de 2 points, maintenant tu as ",courage, "de courage")
    print("malgrés ta fuite , Hagride fait 3metre et court plus vite que toi , il t'a rattrapé")
elif O == 3:
    intelligence = intelligence - 2
    print("Hagride te met un couts tu la tête, tu perd donc 2 point d'intelligence mais tu gagnes 1 points de courage, maintenant tu as ",intelligence,"d'intelligence et tu as aussi",courage,"de courage")

print("Hagride t'emmene dans un magasins et sorcellerie et te demande d'acheter ce que tu veux avec 100 galions ( il te demande d'avoir au minimum : une baguette de soricer , une cape de sorcier et un livre de sort ""\n")
print ("la liste d'objet disponible est : ")
print ("Baguette magique - 35 galions (1)")
print ("Robe de sorcier - 20 galions (2)")
print("Chaudron en étain - 15 galions (3)" )
print("Manuel de potions - 25 galions (4)")
print ("Plume magique - 5 galions (5)")
print ("Livre enchanté - 30 galions (6)")
print ("Balance de cuivre - 10 galions (7)")
print ("Cape d'invisibilité - 100 galions (8)")



