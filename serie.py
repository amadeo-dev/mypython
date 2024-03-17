tailleserie = int(input("Quelle est la taille de ta série de nombres : "))
toto = 0
liste = []
while tailleserie > toto:
    valeur = input("Entre une valeur : ").strip()
    if valeur != "": 
        liste.append(valeur) 
        toto = toto + 1
    else:
        i = 0 
mini = min(liste)
maxi = max(liste)
print("Minimum : ", mini, "Maximum : ", maxi)