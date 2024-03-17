import os
import datetime



def getTime():
    datetimeObject = datetime.datetime.now()
    return datetimeObject.hour

def bjr(nom):
    if getTime() > 18:
        print("Bonsoir", nom)
    else: 
        print("Bonjour", nom, "! Heureux de vous revoir.")

if not os.path.isfile("noms.txt"):
    fich_nom = open("noms.txt", "w")
    nomdumec = input("Quel est ton nom ?")
    fich_nom.write(nomdumec)
    

else:
    fich_nom = open("noms.txt", "r")
    nomdumec = fich_nom.read()
    verif = input("Comment vous appelez vous ?")
    if verif == nomdumec:
        bjr(nomdumec)
    elif verif != nomdumec:
       print("ACCES REFUSE")


