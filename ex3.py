pierre=1
feuille=2
ciseaux=3
score1=0
score2=0
print("1-pierre \n2-feuille \n3-ciseaux")

while score1 or score2 == 3:
 choix = int(input("Choix J1:>"))
choix2 = int(input("Choix J2:>"))
if choix ==1 and choix2 == 3:
    score1=+1

if choix ==2 and choix2 == 3:
    score2=+1

if choix == 1 and choix2 == 2:
    score1=+ 1

if choix == 2 and choix2 == 1:
    score1 = +1

if choix == 3 and choix2 == 2:
    score2 = +1

if choix == 3 and choix2 == 1:
    score1 = + 1

print("score J1=", score1, "score J2=", score2)

