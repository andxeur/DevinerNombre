import random

nbr_cacher = random.randint(0, 10)

while True:

    nbr = int(input("devine le nbr cacher entre 0 et 10 : "))
    if nbr == nbr_cacher:
        print(f"felicitaion vous avez trouver le nbr cacher qui etait : {nbr_cacher}")
        break
    elif nbr > nbr_cacher:
        print("votre nombre est supperieur ")
    elif nbr < nbr_cacher:
        print("votre nombre est inferieur ")
