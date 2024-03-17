import time 
from random import randrange

count = 0
temps = time.time()
temps_tot = 0
while count < 5:
    enter = input("Veuillez entrer un mot au hasard: ")
    temps_act = time.time() - temps
    count += 1
    temps_tot = temps_tot + temps_act

temps_moyen = temps_tot / 5
print("Le temps moyen est %.3f" % temps_moyen, "secondes.")