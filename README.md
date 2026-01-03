README  (Dépôt Final)
Présentation générale
Titre
Projet Poudelard : L’Art de Coder comme un Sorcier
Description
Jeu d’aventure textuel en Python inspiré de Harry Potter. Le joueur crée son personnage, découvre Poudlard, apprend des sorts, passe un quiz et vit une conclusion (match de Quidditch ou scénario libre). Le projet utilise : fonctions, dictionnaires, JSON, aléatoire, modularisation.
Contributeurs
Mendo Hans Parker Groupe sc5
Yoganathan Laurent Groupe sc5
Romain Pinard Groupe sc5
Installation
Cloner le dépôt :
Clonage du Projet avec PyCharm 1. Ouvrez PyCharm 2. Sur l'écran d'accueil, cliquez sur "Get from VCS" 3. Sélectionnez "Git" 4. Entrez l'URL du repository sur git 5. Choisissez le répertoire local où cloner le projet 6. Cliquez sur "Clone"
Lancer le jeu :
Pour lancer le jeu il suffit a partir de l’arborescence du projet d’aller dans utils -> main.py les fonctions qui lancent chaque chapiter y sont deja agencées donc il suffit juste de lancer la lecture de la function main
Utils -> main.py
1.5. Fonctionnalités principales
- Gestion des saisies (input_utils.py)
- Création du personnage (personnage.py)
- Gestion des maisons (maison.py)
- Chapitres 1 à 4 (narration + mini‑jeux)
- Lecture des données JSON
- Menu principal et navigation
Journal de bord
Chronologie
- Semaine du 5 décembre  : structure + input_utils + personnage + chapitre 1
- Semaine du 21 décembre : maison + chapitre 2 + menu/main  , chapitre 3 + début chapitre 4
- Semaine du 3 janvier : finalisation chapitre 4 + intégration + README
Répartition des taches
Mendo Hans Parker:  Chapitre 2
Yoganathan Laurent : chapitre 1 et chapitre 4
Romain Pinard: chapitre 3
Les fonctions de utils maison.py et personage.py ont été traitée ensemble
(par souci avec pycharm l’on a du parfois travailler sur un seul compte)

Contrôle, tests et validation
3.1. Gestion des erreurs
- Vérification des saisies texte (non vide)
- Vérification des nombres (bornes + reconstruction manuelle)
- Menus sécurisés via demander_choix
- Lecture JSON via load_fichier
3.2. Tests effectués
- Création du personnage + achats
- Répartition dans les maisons
- Quiz magique (0 à 4 bonnes réponses)
- Match de Quidditch (avec/sans capture du Vif d’Or)
- test sur l’ensemble des fonctions du projet via le test de main.py
3.3. Bugs connus
- bugs sur le pull le projet a été enormément ralentis à cause de ça
- bugs sur la connexion au compte du coté de Romain
