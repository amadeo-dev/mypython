import io

file = io.open("faq_informatique.txt", 'r', encoding='1252')
question = input("Votre question sur l'informatique : ")
lines = file.readlines()

for i in range(len(lines)):
    q = lines[i]
    if q == question + '\n':
        print(lines[i +1])



