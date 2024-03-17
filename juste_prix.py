from random import randint
import os
clear = lambda: os.system('cls')

def exercice1():
    clear()
    print("Le juste prix, il faut deviner le nombre aleatoire qui a été généré")
    rand = randint(0,20)
    cpt = 5
    print("Vous avez 5 tentatives")
    while cpt != 0:
        user = int(input("Votre proposition :> "))
        if user > rand:
            print("Plus petit")
        elif user < rand:
            print("Plus grand")
        else:
            print("Bien vu!")
            exit()
        print("Il vous reste ", cpt - 1, " tentatives")
        cpt = cpt - 1
    print("Le nombre est :> ", rand)
    exit()

def exercice2():
    clear()
    print("Calculatrice")
    print("1- Addition")
    print("2- Soustraction")
    print("3- Multiplication")
    print("4- Division")

    choix = input("Votre choix :> ")
    if choix == "1":
        print("Vous avez choisi l'addition")
        a = int(input("a = "))
        b = int(input("b = "))
        print("La somme de ", a, " et ", b, "donne :> ", a+b)
    elif choix == "2":
        print("Vous avez choisi la soustraction")
        a = int(input("a = "))
        b = int(input("b = "))
        print("La soustraction de ", a, " par ", b, "donne :> ", a-b)
    elif choix == "3":
        print("Vous avez choisi la multiplication")
        a = int(input("a = "))
        b = int(input("b = "))
        print("La multiplication de ", a, " par ", b, "donne :> ", a*b)
    elif choix == "4":
        print("Vous avez choisi la division")
        a = int(input("a = "))
        b = int(input("b = "))
        if b <= 0:
            while b <= 0:
                print("Il faut que b > 0")
                b = int(input("b = "))
        print("La division de ", a, " par ", b, "donne :> ", a/b)
    else:
        exit()


def exercice3():
    """
    Pierre = 0, Feuille = 1, Ciseaux = 2
    1- La pierre écrase les ciseaux et gagne. 
    2- La feuille enveloppe la pierre et gagne. 
    3- Les ciseaux découpent la feuille et gagnent.
    """
    clear()
    print("Pierre - Feuille - Ciseaux")
    print("""Pierre = 0, Feuille = 1, Ciseaux = 2
    1- La pierre écrase les ciseaux et gagne. 
    2- La feuille enveloppe la pierre et gagne. 
    3- Les ciseaux découpent la feuille et gagnent.""")
    ia = randint(0,2)
    user = int(input("Votre choix :> "))

    cpt = 0
    user_pts = 0
    ia_pts = 0

    while cpt != 2:
        if user == 0 and ia == 2 or user == 1 and ia == 0 or user == 2 and ia == 1:
            if user == 0 and ia == 2:
                print("Pierre VS Ciseaux")
            elif user == 1 and ia == 0:
                print("Feuille VS Pierre")
            else:
                print("Ciseaux VS Feuille")
            print("+1 points pour toi!")
            user_pts = user_pts + 1
        elif user == ia:
            print("Egalite, 0pts")
            cpt = cpt - 1
        else:
            if user == 0 and ia == 1:
                print("Pierre VS Feuille")
            elif user == 1 and ia == 2:
                print("Feuille VS Ciseaux")
            else:
                print("Ciseaux VS Pierre")
            print("Perdu, l'IA gagne +1 pour lui")
            ia_pts = ia_pts + 1
        cpt = cpt + 1
        ia = randint(0,2)
        while True:
            user = int(input("Votre choix :> "))
            if user >= 0 and user < 3:
                break
    
    if user_pts > ia_pts:
        print("Vous avez gagne la partie!")
    else:
        print("Perdu, l'adversaire est meilleur que vous!")
    exit()



def main():
    clear()
    print("""MENU

    1- Exercice 1 (Le juste prix)
    2- Exercice 2 (La calculatrice)
    3- Exercice 3 (Pierre Feuille Ciseaux)
            """)
    
    menu_choix = int(input("Votre choix :> "))
    if menu_choix == 1:
        exercice1()
    elif menu_choix == 2:
        exercice2()
    elif menu_choix == 3:
        exercice3()
    else:
        while menu_choix != 1 or menu_choix != 2 or menu_choix != 3:
            menu_choix = int(input("Votre choix :> "))
            if menu_choix == 1:
                exercice1()
            elif menu_choix == 2:
                exercice2()
            elif menu_choix == 3:
                exercice3()


if __name__ == "__main__":
    main()