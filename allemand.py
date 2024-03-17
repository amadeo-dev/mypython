#import csv 
#dico_csv = open("/Users/Amadeo/Desktop/informatique/python/à_transfert/voc_allemand.csv" , "r") # ouvrir le fichier
#dico = csv.DictReader(dico_csv , delimiter = ",") # initialisation d’un lecteur de fichier avec création automatique de dictionnaire
#for ligne in dico : # parcours du lecteur avec une boucle
#    print(ligne) # affichage ligne à ligne
#dico_csv.close()
fr_all = {"les habitudes alimentaires": "die Essgewohnheiten",
"le végétarien" : "der Vegetarier",
"le végétalien": "der Veganer",
"se nourrir": "sich ernähren",
"végétal": "pflanzlich",
"le restaurant": "die Gaststätte",
"se retrouver pour aller déjeuner": "sich zum Essen verabreden",
"la spécialité": "die Spezialität",
"la gastronomie": "die Gastronomie",
"le bistrot": "die Kneipe",
"le produit d'origine animal": "das Tierprodukt",
"la colocation": "die Wohngemeinschaft",
"économiser": "sparen",
"le colocataire": "der Mitbewohner",
"l'étudiant": "der Student",
"l'étudiante": "die Studentin",
"les étudiants": "die Studenten",
"entreprendre": "unternehmen",
"solitaire": "einsam",
"une chambre à soi": "ein eigenes Zimmer",
"qui tient lieu de famille" : "die Ersatzfamilie",
"le pays natal" : "die Heimat",
"la ville natale": "die Heimatstadt",
"être locataire": "zur Miete wohnen",
"les meubles": "die Möbel",
"l'appartement": "die Wohnung",
"louer": "mieten",
"l'aménagement": "die Einrichtung",
"confortable, agréable": "gemütlich",
"inviter qn à dîner": "jemanden zum Abendessen einladen",
"se sentir bien": "sich wohl fühlen",
"avoir peu de place": "wenig Platz haben",
"passer beaucoup de temps à la maison": "viel Zeit zu Hause verbringen",
"embellir": "verschönern",
"cuisiner": "kochen",
"nettoyer": "putzen",
"le snack": "der Imbiss",
"le gourmet": "der Feinschmecker",
"le plat": "das Gericht",
"varié": "vielfültig",
"le chez-soi": "das Zuhause",
"la musculation": "der Kraftsport",
"le métier": "der Beruf",
"les études": "das Studium",
"le pays frontalier": "das Nachbarland",
"l'influence": "der Einfluss",
"influencer": "beeinflussen",
"la cuisine": "die Küche",
"d'un côté ... de l'autre côté": "einerseits ... andererseits",
"clair": "hell",
"l'abri de plage": "der Strandkorb",
"le pain d'épice": "der Lebkuchen",
"auf etwas verzichten": "renoncer à qc"}

dico = {"die Essgewohnheiten": "les habitudes alimentaires","der Vegetarier": "le végetarien",
"der Veganer": "le végetalien",
"renoncer à qc": "auf etwas verzichten",
"sich ernahren": "se nourrir",
"pflanzlich": "végetal",
"die Gaststatte": "le restaurant",
"sich zum Essen verabreden": "se retrouver pour aller déjeuner",
"die Spezialitat": "la specialite",
"die Gastronomie": "la gastronomie",
"die Kneipe": "le bistrot",
"das Tierprodukt": "le produit d'origine animal",
"die Wohngemeinschaft": "la colocation",
"sparen": "économiser",
"der Mitbewohner": "le colocataire",
"der Student": "l'étudiant",
"die Studentin": "l'étudiante",
"die Studenten": "les étudiants",
"unternehmen": "entreprendre",
"einsam": "solitaire",
"ein eigenes Zimmer": "une chambre a soi",
"die Ersatzfamilie": "qui tient lieu de famille",
"die Heimat": "le pays natal",
"die Heimatstadt": "la ville natale",
"zur Miete wohnen": "être locataire",
"die Mobel": "les meubles",
"die Wohnung": "l'appartement",
"mieten": "louer",
"die Einrichtung": "l'amenagement",
"gemutlich": "confortable, agréable",
"jemanden zum Abendessen einladen": "inviter qn a dîner",
"sich wohl fuhlen": "se sentir bien",
"wenig Platz haben": "avoir peu de place",
"viel Zeit zu Hause verbringen": "passer beaucoup de temps à la maison",
"verschonern": "embellir",
"kochen": "cuisiner",
"putzen": "nettoyer",
"der Imbiss": "le snack",
"der Feinschmecker": "le gourmet",
"das Gericht": "le plat",
"vielfaltig": "varié",
"das Zuhause": "le chez-soi",
"der Kraftsport": "la musculation",
"der Beruf": "le metier",
"das Studium": "les études",
"das Nachbarland": "le pays frontalier",
"der Einfluss": "l'influence",
"beeinflussen": "influencer",
"die Kuche": "la cuisine",
"einerseits ... andererseits": "d'un cote ... de l'autre coté",
"hell": "clair",
"der Strandkorb": "l'abri de plage",
"der Lebkuchen": "le pain d epice"}

print("            ///Dictionnaire français_allemand///")
choix = input("A-allemand->français ou B-français->allemand : ")
if choix == 'A':
    a = True
    def recherche(recherche):
        recherche = input("Rechercher dans le dictionnaire : ")
        return dico[recherche]
    while a:
        print(recherche(recherche))
else:
    a = True
    def recherche(recherche):
        recherche = input("Rechercher dans le dictionnaire : ")
        return fr_all[recherche]
    while a:
        print(recherche(recherche))






    



