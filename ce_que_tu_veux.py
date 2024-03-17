# import random 
# #ex 1:
# a = 2 #int
# b = "Salut tout le monde" # chaîne de caractères
# c = ["Bonjour", "salut", "coucou"] #liste
# d = True #boolean
# e = 2.7 #float
# f = 'A'

# #ex2:
# #trouver le nombre le plus petit d'une liste.
# liste = [2, 7, 9, 3, 6]
# a = liste[0] 
# for nbr in liste:
#     if nbr < a:
#         a = nbr
# print(a)

# #ex3
# vie = 3
# while vie > 0:
#     nombre_aleatoire = random.randint(0, 9)
#     joueur = int(input("Choisi un nombre :"))
#     if joueur == nombre_aleatoire:
#         print("GG")
#         break
#     else:
#         print("dommage")
#         vie = vie - 1
#     if vie == 0:
#         print("T'es nul.")
#ex4 Amadéo
def plr(sing):
    if sing[-2:] == "au":
        sing = sing + 'x'
    elif sing[-2:] == "al":
        sing = sing[:-2] + "aux" 
    else:
        sing = sing + 's'
    return sing
print(plr(input("Quel mot veut tu mettre au pluriel?")))

