print("___CALCULATRICE___")

Addition=1
Soustraction=2
Multiplication=3
Division=4

print("1-Addition \n2-Soustraction \n3-Multiplication \n4-Division")

Methode = int(input("Votre choix :>"))

if Methode == 1:
     print("Vous avez choisi l'addition ")
     a = int(input("a = "))
     b = int(input("b = "))
     print("La somme de " ,a ,"et",b ,"donne:>", a + b )
     print("\n")

if Methode == 2:
    print("Vous avez choisi la soustraction")
    a = int(input("a = "))
    b = int(input("b = "))
    print("La différence de ", a, "et", b, "donne:>", a - b)
    print("\n")


if Methode == 3:
    print("Vous avez choisi la multiplication ")
    a = int(input("a = "))
    b = int(input("b = "))
    print("Le produit de ", a, "et", b, "donne:>", a * b)
    print("\n")


if Methode == 4:
    print("Vous avez choisi la division ")
    a = int(input("a = "))
    b = int(input("b = "))
if a == 0.0:
        print("Divier par 0 est impossible")
if b == 0.0:
            print("Divier par 0 est impossible")
else :
    print("Le quotient de ", a, "et", b, "donne:>", a / b)
    print("\n")



