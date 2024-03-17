# Exo 1
# Ecrire: un int, un float, un string, une liste, un boolean et un char.
a = 10 # int => nombre entier
b = 5.15 # float => nombre decimal
c = "Hello" # string => chaîne de caractères
e = [1, "a", 3, 25.2] # list => liste d'élements
f = True # boolean => Vrai ou Faux
g = 'a' # char => caractère

# Exo 2
# Récuperer le nombre le plus petit d'une liste en utilisant une boucle for.
# /!\ Pas le droit à la fonction min.
liste = [3, 8, 1, 3]
plus_petit_nombre = liste[0]
for element in liste[1:]:
    if element < plus_petit_nombre:
        plus_petit_nombre = element
print(plus_petit_nombre)


# print(plus_petit_nombre)
# Exo 3
# Créer un mini jeu de loto ou il faut donner un nombre et voir si ce nombre est
# égal au nombre aleatoire, la personne a 3 chances.
# astuce : pour générer un nombre aleatoire entre 0 et 9:
import random
nombre_aleatoire = random.randint(0, 9)
chance = 3
while chance > 0:
    nombre_utilisateur = int(input("Rentrer un nombre entre 0 et 9 inclus: "))
    if nombre_utilisateur == nombre_aleatoire:
        print("Bravo !")
        break
    else:
        chance -= 1
        print(f"Tu as perdu une vie, chance restante: {chance}.")

# Exo 4
# Créer une fonction qui prend un mot au singulier et qui le transforme en pluriel.
# (Je donnerais 10 mots au hasard et je verrais votre function elle donne combien
# de bonne reponses)
# La fonction s'appelle 'to_plural' prend un string en entrer et renvoie un string
# Attention, tous les mots ne finissent pas par "s" au pluriel
# astuce : concatener des string

def to_plural(mot):
    if mot[-2:] == "al":
        mots = mot[:-2] + "aux"
    elif mot[-2:] == "au":
        mots = mot + "x"
    elif mot[-3:] == "eux":
        mots = mot
    else:
        mots = mot + "s"
    return mots

print(to_plural("cheval")) # chevaux
print(to_plural("garçon")) # garçonx
print(to_plural("dangereux")) # dangereux

# Exo 5
# Faire une fonction qui prend en entrer une liste de jeux et qui renvoie en sortie
# un jeu au hasard quand vous hesitez à quoi jouer.
# La fonction s'appelle 'choisis_pour_moi_parmis_' prend une liste de string en entrer et
# renvoit un string


# Les dictionnaires