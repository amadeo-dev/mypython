from random import randrange

nbr = input("Veuillez choisir un nombre entre 0 et 20: ")
a, b = 0, 20
prop = randrange(a,b)
rep = ''

while rep != "=":
    prop = (a + b)//2
    print(prop)
    rep = input("Entrer + ou - ou =:")
    if rep == "+":
        a = prop
    if rep == "-":
        b = prop
    if rep == "=":
        print("!!!BRAVO!!!")

    

    

