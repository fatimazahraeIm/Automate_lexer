# Projet Automate

Ce projet implémente un automate à états finis (FA) et permet de générer une représentation procédurale directe de cet automate. Il permet également de vérifier si une expression suit cet automate, c'est-à-dire de vérifier si cette expression est correcte lexicalement.

## Fonctionnalités

- **Ajout d'états** : Vous pouvez ajouter des états à l'automate, en spécifiant s'ils sont des états finaux ou non.
- **Ajout de transitions** : Vous pouvez ajouter des transitions entre les états en spécifiant le symbole de transition.
- **Génération de la représentation procédurale** : Le projet génère une représentation procédurale de l'automate sous forme de fonctions en C.
- **Analyse lexicale** : Vous pouvez vérifier si une chaîne de caractères suit l'automate en effectuant une analyse lexicale.

## Utilisation

1. **Définir l'alphabet** : L'utilisateur est invité à entrer l'alphabet de l'automate.
2. **Ajouter des états** : L'utilisateur peut ajouter des états et spécifier s'ils sont finaux.
3. **Définir l'état initial** : L'utilisateur doit spécifier l'état initial de l'automate.
4. **Ajouter des transitions** : L'utilisateur peut ajouter des transitions entre les états en spécifiant le symbole de transition.
5. **Générer la représentation procédurale** : Le projet génère une représentation procédurale de l'automate.
6. **Analyse lexicale** : L'utilisateur peut entrer une chaîne de caractères pour vérifier si elle suit l'automate.

Veuillez consulter le rapport et la video de démonstartion pour plus de détails:
[Lien vers la vidéo de démonstration](./DemoVideo.mp4)


```sh
python Automate.py

