from random import randrange
import webbrowser
import time

salam = ["salut", "bonjour", "cc", "slt", "hello", "hi", "salam"]
bye = ["au revoir", "à la revoyure", "bye"]
noms = ["gabriel", "amadéo", "noa", "gauthier", "clément", "kilian", "maxime", "alexandre"]

print("Bienvenue dans ce logiciel de simulation conversationelle.")

while 1:
    enter = input(":")
    enter = enter.lower()
    
    if enter in salam:
        salutation = salam[randrange(len(salam))]
        print(salutation, "c'est quoi ton ptit nom toi;)?")

    elif enter in noms:
        nom = enter
        print("Ohh fantastique", nom, ", tu as un très beau prénom.")
        print("As-tu des questions?'o/n")

    elif enter in bye:
        alr = bye[randrange(len(bye))]
        print(alr, nom)
        break
    
    elif enter == 'o':
        print("Tu devrais chercher sur internet. Google est ton ami.")
        time.sleep(2)
        webbrowser.open('https://google.com')
    
    elif enter == 'n':
        print("Tant mieux je n'aurais pas pu y répondre.")

    else:
        print("Désolé, je n'ai pas compris.")
