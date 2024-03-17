def retrouve1(tableau):
    return tableau.count(1)

tableau = [1, 3, 17, 88, 64, 1, 90, 43, 1, 5 , 1, 72]#int(input("Entre un tableau:"))
            # (jsp comment faire rentrer un tableau à l'utilsateur)
print("Il y a: " , retrouve1(tableau) , " chiffres 1 dans le tableau")