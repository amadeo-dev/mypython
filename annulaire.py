a = {
    "Jean": "06 72 28 37 17",
    "Pierre": "07 81 25 37 84",
    "Patrick": "06 54 37 98 10",
}
def add(a, nom, num):
    a[nom] = num

add(a, "Simon", "06 17 27 38 29")

def delete(a, items):
    del a[items]
delete(a, "Jean")

def show(a):
    print("PAGE JAUNE:")
    for i, o in a.items():
        print(i, '->', o)

azerty = 0
for i in a:
    azerty = azerty + 1
print("Il y a", azerty,"éléments dans l'annulaire.")

