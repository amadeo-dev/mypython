

# Exo 1
# Exercice => variable a qui est un booléen vrai
a = True
print(a)

# Exo 2
# Si a est vrai bonjour sinon au revoir
if a:
    print("bonjour")
else:
    print("aurevoir")

if a == True:
    print("bonjour")
else:
    print("aurevoir")

if a is True:
    print("bonjour")
else:
    print("aurevoir")

if not a:
    print("aurevoir")
else:
    print("bonjour")

# Exo 3
# Créer un tableau avec les éléments 1, 2, 3 et 4
tableau = [1, 2, 3, 4]

# Exo 4 Kevin => Amadeo => Ilian
# Ecrire un commentaire "c'est un tableau"
tableau = [1, 2, 3, 4] # c'est un tableau

# Exo 5
# Parcourir le tableau et affiché les éléments

for element in tableau: # Pour chaque element dans la liste tableau
    print(element)      # Afficher l'élément

# Exo 6
# Additionner tous les éléments de votre liste

# Créer une variable "total" qui est égale 0
# Pour chaque élément du tableau ou rajoute à "total" la valeur de l'élément
# On affiche le total

total = 0
tableau = [1, 2, 3, 4]
for element in tableau:
    total = total + element # ou total += element
print(total)

# Exo 7
# Multiplier tous les éléments de votre liste
total = 0
taille = 0
tableau = [1, 2, 3, 4]
for element in tableau:
    total = total * element
print(total)


# Exo 7 Bonus
# Multiplier tous les éléments de votre liste et diviser par le nombre d'éléments du tableau
total = 0
taille = 0
tableau = [1, 2, 3, 4]
for element in tableau:
    total = total * element
    taille = taille + 1
print(total / taille)


# Exo 8
# Créer une fonction qui additionne deux chiffres et qui retourne le resultat => addition
def addition(chiffre_1, chiffre_2):
    return chiffre_1 + chiffre_2

print(addition(1, 2))
print(addition(3, 5))

# Exo 9
# Créer une fonction qui prend en argument des minutes et qui les transforment en secondes => to_second
def to_second(minutes):
    return minutes * 60

print(to_second(10))
print(to_second(30))

# Exo 10 x2 
# Créer une function qui prend en argument un tableau de minutes, qui le transforme en seconde et qui 
# additionne toutes les secondes et qui retourne le resultat => yolo
tableau = [1, 2, 3, 4] # 1 minute, 2 minutes, 3 minutes et 4 minutes

def yolo(les_minutes):
    total = 0
    for minutes in les_minutes:
        total = total + to_second(minutes)
    return total

print(yolo(tableau))