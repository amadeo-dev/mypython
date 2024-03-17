import time 
from random import randrange

count = 0

temps_tot = 0
liste = ["critere", "dehors", "faucon", "afflux", "accort", "bijoux", "angle", "armoire", "banc", "bureau", "cabinet", "carreau", "chaise", "classe", "clé", "coin", "couloir", "dossier", "eau",
    "école", "écriture", "entrée", "escalier", "étagère", "étude", "extérieur", "fenêtre", "intérieur", "lavabo", "lecture", "lit", "marche",
    "matelas", "maternelle", "meuble", "mousse", "mur", "peluche", "placard", "plafond", "porte", "portemanteau",
    "poubelle", "radiateur", "rampe", "récréation", "rentrée", "rideau", "robinet"]

while count < 5:
    temps = time.time()
    r = randrange(0, len(liste))
    trouve = liste[r]
    enter = input("Mot à taper : " + trouve + ": ")
    
    while enter != trouve:
        enter = input("Je répéte, le mot à taper est : "+ trouve + ": ")


    t_caract_moy = (time.time()- temps)/len(trouve) 
    print("Le temps de frappe moyen est:", t_caract_moy,)
    temps_act = time.time() - temps
    temps_tot = temps_tot + temps_act

    count += 1
    


temps_moyen = temps_tot / 5
print("Le temps moyen est %.3f" % temps_moyen, "secondes.")