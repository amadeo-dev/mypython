import os
from random import randrange

n = randrange(0, 49)
argent = 500
print("---------------------------------------------------------")
print("                                                          ")
print("wsh mon frr bienvenu au jeu de la roulette")
print("Vous avez", argent, "€")
mise = int(input("Mise un nombre entre 0 et 50:"))
somme = int(input("Mise une somme:"))
if somme > argent:
    print("Tu n'as pas assez d'argent,va travailler")
    print("relance le jeu pcq là je sais pas comment faire pour que ça se fasse auto")
if mise < 0:
    print("ta mise est inferieur à 0 recommence frr")
    print("relance le jeu pcq là je sais pas comment faire pour que ça se fasse auto")
else:
    print("La roulette est tombé sur", n);

    if mise == n:
        print("waaa gg tu gagne le double de ta mise")
        argent = mise * 2
    elif mise == n and n%2:
        print("GG la roulette est tombé sur la meme couleur que ta mise ,tu gagnes la moitié de ta mise")
    else:
        print("DSL t'as perdu")
        continuer = True
        while continuer:
            print("Tu as à présent", argent, "€ ")
            choix = input("Voulez vous continuer ? ")
            print(choix)
            if choix != 'oui':
                break




                form = "{0:10}{1:10}{2:10}"
                for val in T:
                    print
                    form.format(*val)
