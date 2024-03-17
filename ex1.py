from random import randrange
n = randrange(0,50)
vies = 5
indice = "?"
while vies > 0:
    écris = input("Ton nombre:")
    écris = int(écris)
    if écris < n :
        indice = "trop bas"
        print("Vies:" ,vies, "-->Ton nombre est", indice)
    else :
        indice = "trop haut"
        print(" Vies:" ,vies, "-->Ton nombre est", indice)
    if écris == n:
        indice = "bravo !"
        print(vies, écris, indice)
        break
if vie==0:
    print("Tou a perdou zeubi")
    vies -= 1
