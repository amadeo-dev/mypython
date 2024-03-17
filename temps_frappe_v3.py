import time 
from random import randrange


def game():
    count = 0
    temps_tot = 0
    liste = ["critere", "dehors", "faucon", "afflux", "accort", "bijoux", "angle", "armoire", "banc", "bureau", "cabinet", "carreau", "chaise", "classe", "clé", "coin", "couloir", "dossier", "eau",
    "école", "placard", "plafond", "porte", "portemanteau", "poubelle", "radiateur", "rampe", "récréation", "rentrée", "rideau", "robinet"]

    temps = time.time()

    while count < 5:
        r = randrange(0, len(liste))
        trouve = liste[r]
        enter = input("Mot à taper : " + trouve + ": ")
        
        while enter != trouve:
            enter = input("Je répéte, le mot à taper est : "+ trouve + ": ")

        count += 1
    temps_tot = time.time() - temps
    return temps_tot

def load_highscore():
    file = open("score.txt", 'r')
    highscore = file.read()
    return highscore

def save_highscore(a):
    highscore = float(load_highscore())
    if a < highscore:
        nom = input("Quel est votre nom ?")
        file = open("score.txt", 'a')
        file.write( "\n ["    +   str(a)   +    ",'"    + nom +"']")
        file.close()


a = game()
save_highscore(a)
print("Votre score est :", a)
print("Le meilleur résultat est : ", load_highscore())

    