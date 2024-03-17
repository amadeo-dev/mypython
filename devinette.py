from random import randint
import sys
rand = randint(0,20)
print("------------ Choisissez un nombre entre 1 et 20 -----------------")
ndc=5
ndc1=5

j1 = int(input("Nombre j1 :> "))
j2 = int(input("Nombre j2 :> "))
if j1 > 20:
    print('!! j1: ton nombre est trop grand')
if j2 > 20:
    print('!! j2: ton nombre est trop grand')

while j1 >20 or j2 >20:
    j1 = int(input("Nombre j1 :> "))
    j2 = int(input("Nombre j2 :> "))
    if j1 > 20:
        print('!! j1: ton nombre est trop grand')
    if j2 > 20:
        print('!! j2: ton nombre est trop grand')

if j1 - rand > j2 - rand:
    print("*j2 est plus près")
    ndc = ndc - 2
    ndc1 = ndc1 + 2
    print("*J1 a encore", ndc, "coup ---", "J2 a encore", ndc1, "coup")
else:
    print("*j1 est plus près")
    ndc = ndc + 2
    ndc = ndc1 - 2
    print("*J1 a encore", ndc, "coup ---", "J2 a encore", ndc1, "coup")

while ndc != 0 or ndc1 != 0:
    j1 = int(input("Nombre j1 :> "))
    j2 = int(input("Nombre j2 :> "))
    if j1 > 20:
        print('!! j1: ton nombre est trop grand')
    if j2 > 20:
        print('!! j2: ton nombre est trop grand')

    elif j1  > rand and j2 > rand:
        print("-j1 et j2 sont trop grand")
        ndc = ndc - 1
    elif j1 < rand and j2 < rand:
        print("-j1 et j2 sont trop petit")
        ndc = ndc - 1
    elif j2 < rand and j1 > rand:
        print("-j1 est trop grand.")
        print("-j2 est trop petit")
        ndc = ndc - 1
    elif j1 < rand and j2 > rand:
        print("-j1 est trop petit")
        print("-j2 est trop grand.")
        ndc = ndc - 1

    elif j1 == rand:
        print("(c'est j1 qui a TROUVE)")
        ndc = ndc - 1
    elif j2 == rand:
        print("(c'est j2 qui a TROUVE)")
        ndc = ndc - 1
    if j1 == rand or j2 == rand:
        sys.exit("Le nombre mytère a été trouvé, c'est fini!")

