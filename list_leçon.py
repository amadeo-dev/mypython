characters = ["Kaneki", "Toka", "Naruto", "Shisui", "Asta"]#créé liste
characters.remove("Shisui")#supprimer Sisui
characters.insert(4, "Shu")#inserer Shu à la 4eme place
characters[1] = "Bob le bg"#remplacer le 1 élément(Toka)(pcq on compte à partir de 0)par "Bob le bg"
characters.pop(3)#suppr 3eme élément (ici 'Asta')
print("Il y a ", len(characters), "éléments dans la liste.")#affiche la taille de la liste
characters.append("Itachi")#ajoute 'Itachi' à la fin de la liste
print(characters.index("Kaneki"))#afiche la position de 'Kaneki dans la liste
print(characters)

