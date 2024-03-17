# exerice 6:
# je vous donne la hauteur d'un fond marin calcule le volue d'eau necesaire pour
# remplire celui ci.
# exemple:
#
#  ^
# 4|           █
# 3|    █      ██
# 2| █  █   ██ ██
# 1|██  ███████████
# 0---------------->
# representation sous forme de liste
# height = [1,2,0,3,1,1,1,2,2,1,4,3,1,1]
#
#  ^
# 4|░░░░░░░░░░░█░░░
# 3|░░░░█░░░░░░██░░
# 2|░█░░█░░░██░██░░
# 1|██░░███████████
# 0---------------->
# fill(height) => 37

def fill(height):
    taille = len(height)* max(height)
    eau = taille - sum(height)
    return eau

height = [1,2,0,3,1,1,1,2,2,1,4,3,1,1]
print(fill(height))


#exercice 7:
# On se trouve maintent sur la terre ferme il pleut, des flaques se forment.
# on vous donne la hauteur du terain (comme pour l'exerice 6) trouvez la taille
# de toutes les flaques
# exemple:
#
#  ^
# 3|       █
# 2|   █   ██ █
# 1| █ ██ ██████
# 0---------------->
# representation sous forme de liste
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#
#  ^
# 3|       █
# 2|   █░░░██░█
# 1| █░██░██████
# 0---------------->
# puddle(height) => 6
def puddle(height):
    
    return 0

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]