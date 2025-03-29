# Jeu de Devinette


Ce code implémente un jeu de devinette simple où l'utilisateur doit deviner un nombre caché compris entre 0 et 10.

## Fonctionnement

1. Le code génère un nombre aléatoire `nbr_cacher` compris entre 0 et 10 à l'aide de la fonction `random.randint`.
2. L'utilisateur est invité à deviner le nombre caché en saisissant un nombre compris entre 0 et 10.
3. Si l'utilisateur devine correctement le nombre caché, le code affiche un message de félicitations et se termine.
4. Si l'utilisateur saisit un nombre supérieur au nombre caché, le code affiche un message indiquant que le nombre saisi est supérieur.
5. Si l'utilisateur saisit un nombre inférieur au nombre caché, le code affiche un message indiquant que le nombre saisi est inférieur.

## Exécution

Pour exécuter le code, il suffit de copier et coller le code dans un interpréteur Python ou de l'enregistrer dans un fichier avec l'extension `.py` et de l'exécuter avec la commande `python nom_fichier.py`.