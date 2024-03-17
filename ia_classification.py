from sklearn import datasets, svm, metrics, tree
import numpy as np
import matplotlib.pyplot as plt

libelle_features = ["poids", "longueur", "nbr_roues", "nbr_moteurs", "électrique"]
    

features = [
    [14,1.8,2,0,0],
    [32,1.7,2,0,0],

    [800,3.4,4,1,0],
    [1500,4.5,4,1,0],

    [340,1.9,2,1,0],
    [200,1.8,2,1,0],

    [3,0.8,2,0,0],
    [3,0.8,3,0,0],

    [150,2.0,4,1,0],
    [100,1.4,4,1,0],

    [2000, 10.0, 6, 1, 0],
    [5100, 9, 8, 1, 0],
#   [2000, 10.0, 12, 1, 0],
#   [3000, 9, 4, 1, 0],

    [0.6, 0.3, 8, 0, 0],
    [3, 0.5, 6, 0, 0],

    [14,1.8,2,0,1],
    [32,1.7,2,0,1],
   ]


libelle_class = ["velo", "voiture", "moto", "trotinette", "quad", "camion", "rollers", "velo-éléctrique"]
#dictClass = ["velo", "voiture", "moto", "trotinette", "quad", "camion", "rollers", "velo-éléctrique"]
#dictClass = {0: "velo", 1: "voiture", 2: "moto", 3: "trotinette", 4: "quad", 5:"camion", 6:"rollers", 7:"velo-éléctrique"}
classes = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]

classifier = tree.DecisionTreeClassifier()
#classifier = svm.SVC(gamma='auto')
classifier.fit(features, classes)

new_comers = [9,1.8,2,0,0]
new_comers2 = [4,1.8,2,0, 0]
new_comers3 = [800,3.8,4,1, 0]
new_comers4 = [800,3.8,10,1, 0]
new_comers5 = [2700, 11, 4, 1, 0]
new_comers6 = [2, 0.2, 5, 0, 0]
new_comers7 = [19, 1.9, 2, 0, 1]

predicted = classifier.predict([new_comers, new_comers2, new_comers3, new_comers4, new_comers5, new_comers6, new_comers7])

print("predicted: %s" % str(predicted))
for c in predicted:
    print(""+libelle_class[c])

if 1 :
    tree.plot_tree(classifier , impurity = False , fontsize = 8 ,
                    feature_names = libelle_features , class_names = libelle_class , filled = True , rounded = True,
    )
    plt.show()
