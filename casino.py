import random
import time
argent = 500

def pendu():
    liste = ["critere", "dehors", "faucon", "afflux", "accort", "bijoux", "angle", "armoire", "banc", "bureau", "cabinet", "carreau", "chaise", "classe", "clé", "coin", "couloir", "dossier", "eau",
    "école", "écriture", "entrée", "escalier", "étagère", "étude", "extérieur", "fenêtre", "intérieur", "lavabo", "lecture", "lit", "marche",
    "matelas", "maternelle", "meuble", "mousse", "mur", "peluche", "placard", "plafond", "porte", "portemanteau",
    "poubelle", "radiateur", "rampe", "récréation", "rentrée", "rideau", "robinet"]
    global argent
    mot = random.choice(liste)
    vie = 10
    tiret = ""
    lettres_trouvees = ""
    prop = ['']
    for _ in mot:
        tiret = tiret + "_ "
    print("-----------Jeu du pendu-----------")
    while vie > 0:
        print("Devinez ce mot : ", tiret)
        lettre = input("Proposez une lettre : ")
        if lettre not in prop:
            if lettre in mot:
                lettres_trouvees = lettres_trouvees + lettre
                prop.append(lettre)
                print("C'est ça\n")
            else:
                vie = vie - 1
                prop.append(lettre)
                time.sleep(0.5)
                print("Raté, il vous reste", vie, "tentatives\n")

            for _ in mot:
                if _ in lettres_trouvees:
                    tiret += _ + " "
                else:
                    tiret += "_ "

            if "_" not in tiret:
                print("Bravo vous avez gagné 100€")
                argent = argent + 100
                main()
            elif vie == 0:
                print("Dommage vous avez perdu 😫")
                print('Le mot était :', mot)
                argent = argent - 50
                main()
        else:
            ...
            
def mas():
    global argent
    print("\n----------Bienvenue à la machine à sous----------")
    print("Faites fortune ou perdez tout!")
    print("Règles:")
    print("-Trois chiffres vont êtres tirés au hasard. \n-Si ces trois chiffres correspondent entre eux,"
            " vous gagnerez le triple de ce que avez miser.\n-Si deux chiffres coorespondent, vous gagnerez le double de votre mise.\n")
    mise = int(input("Veuillez miser une somme :"))
    nbr1 = random.randint(1, 10)
    nbr2 = random.randint(1, 10)
    nbr3 = random.randint(1, 10)
    print("La roulette tourne...")
    time.sleep(2.0)
    print("\nLa roulette affiche :", nbr1, nbr2, nbr3)
    time.sleep(1.0)
    if nbr1 == nbr2 == nbr3:
        argent = argent + mise*3
        print("Bravo!! Vous avez gagné le jackpot🥳")
    if nbr1 == nbr2 or nbr1 == nbr3 or nbr2 == nbr3:
        argent = argent + mise*2
        print("Bravo! Vous gagnez le deuxième prix.")
    else:
        argent = argent - mise
        print("Dommage, une prochaine fois peut être.")
    again = input("Voulez vous rejouer ? (o/n)")
    if again == 'o':
        mas()
    else:
        main()

def pfc():
    global argent
    print("-----------Pierre-Feuille-Ciseaux-----------")
    userp = 0
    botp = 0
    while userp or botp < 3:
        user = int(input("Choix de signes :\n 1-Pierre\n 2-Feuille\n 3-Ciseaux\nQuel est votre choix :"))
        bot = random.randint(1, 3)
        if user == 1 and bot == 3 or user == 2 and bot == 1 or user == 3 and bot == 2:
            userp = userp + 1
            print("Vous avez gagnés la manche!\n")
            print("Vous:", userp,"// Bot:", botp)
            time.sleep(0.5)
        elif user == bot:
            print("Egalité.\n")
            print("Vous:", userp,"// Bot:", botp)
            time.sleep(0.5)
        else:
            botp = botp + 1
            print("Vous avez perdu la manche!")
            print("Vous:", userp,"// Bot:", botp)
            time.sleep(0.5)
    if botp == 3:
        print("Vous avez perdue 30€.")
        argent = argent - 30
        time.sleep(0.5)
        main()
    elif userp == 3:
        print("Vous avez gagnés 30€")
        argent = argent + 30
        time.sleep(0.5)
        main()

def jstp():
    global argent
    print("Le juste prix, il faut deviner le nombre aleatoire qui a été généré")
    rand = random.randint(0,20)
    cpt = 5
    print("Vous avez 5 tentatives")
    while cpt != 0:
        user = int(input("Votre proposition :> "))
        if user > rand:
            time.sleep(0.5)
            print("Plus petit")
        elif user < rand:
            time.sleep(0.5)
            print("Plus grand")
        else:
            print("Et boum en plein dans le sanglier!")
            argent = argent + 100
            time.sleep(1.0)
            main()
        print("Il vous reste ", cpt - 1, " tentatives")
        cpt = cpt - 1
    print("Le nombre est :> ", rand)
    if cpt <= 0:
        argent = argent - 100
        print("Et c'est perdu :/")
        main()

def main():
    if argent <= 0:
        print("\nC'est la faillite. Vous avez perdue toute votre argent dans des jeux. Dommage🥲.")
        exit()
    else:
        print("---------Bienvenue au casino--------")
        print('\nVous avez', argent,'€\n')
        choix = int(input("  1-Pendu:\n  2-Machine à sous:\n  3-Pierre,feuille ciseaux\n  4-Le juste prix:\n\nChoisissez votre mode:"))
        if choix == 1:
            pendu()
        elif choix == 2:
            mas()
        elif choix == 3:
            pfc()
        elif choix == 4:
            jstp()
        else:
            while choix != 1 or choix != 2 or choix != 3 or choix != 4:
                menu_choix = int(input("Votre choix :> "))
                if menu_choix == 1:
                    pendu()
                elif menu_choix == 2:
                    mas()
                elif menu_choix == 3:
                    pfc()
                elif choix == 4:
                    jstp()

if __name__ == "__main__":
    main()