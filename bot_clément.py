# Créé par chuang, le 19/01/2023 en Python 3.7
import random
import time

while 1 :
    question = input()

    if question == "Bonjour" or question == "Salut" or question == "yo":
        x=random.randint(1,2)
        if x%2==0:
            print("bonjour")
        else:
            print("Salut")

    elif question == "Comment ça va ?" :
        print ("Bien et toi ?")

    elif question == "une blague stp":
        x=random.randint(1,4)
        if x==1:
            print ("Qu'est ce qu'une tranche de jambon sur un scooter")
            time.sleep(3)
            print ("un antivol, from AMXDEO")
        elif x==2:
            print ("Tu connais la blague du petit dej")
            time.sleep(3)
            print ("pas de bol, from KIKI")
        elif x==3:
            print ("Qu'est ce qui est jaune et qui attend")
            time.sleep(3)
            print ("Jonathan, from MASSIME")
        elif x==4:
            print ("Qu'est ce qui est pire qu'un bebe dans une poubelle ?")
            time.sleep(3)
            print ("2 bebes dans une poubelle, from KIKI")

    elif question == "au revoir" or question == "A plus" :
        print("au revoir")
        break
    else :
        print ("JSP mec t'abuses là")
