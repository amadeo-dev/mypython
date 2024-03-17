compte = 500 #Argent total sur son compte
ans = 0#nombre d'années
while compte < 600:#éffectuer les actions suivantes tant que Maeva a moins de 600€ sur son compte
    compte = compte * 1.04#Augmentation de 0,4% l'argent sur le compte de Maeva
    ans = ans + 1#permet de compter le nombre d'années
    print("Maeva a ", round(compte,2),"€ sur son compte.")#affiche pour chaque année l'argent du compte de Maeva
print("Maeva doit laisser cette somme d'argent placée ", ans,"ans pour disposer d'au moins 600€.")#affiche solution