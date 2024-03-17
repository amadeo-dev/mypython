#  _____       _          _____  _             _                  _____
# |  __ \     | |        |  __ \| |           (_)                / ____|
# | |__) |___ | | ___    | |__) | | __ _ _   _ _ _ __   __ _    | |  __  __ _ _ __ ___   ___
# |  _  // _ \| |/ _ \   |  ___/| |/ _` | | | | | '_ \ / _` |   | | |_ |/ _` | '_ ` _ \ / _ \
# | | \ \ (_) | |  __/   | |    | | (_| | |_| | | | | | (_| |   | |__| | (_| | | | | | |  __/
# |_|  \_\___/|_|\___|   |_|    |_|\__,_|\__, |_|_| |_|\__, |    \_____|\__,_|_| |_| |_|\___|
#                                         __/ |         __/ |
#                                        |___/         |___/


# Exercice n01 : arme
# ecrire une fonction qui cree une arme (`new_weapon`). Une arme a comme
# proprieter :
# - son nom
# - ses degat magique
# - ses degat physique
# - son poids
# - son cout magique
def new_weapon(name, physical_domage, magic_domage, physical_cost, magic_cost):
    return {
        "name": name,
        "physical_domage": physical_domage,
        "magic_domage": magic_domage,
        "physical_cost": physical_cost,
        "magic_cost": magic_cost
    }


# tests
epee = new_weapon("epee", 0, 10, 5, 0)
bagette_magique = new_weapon("bagette magique", 5, 0, 0, 3)
escalibure = new_weapon("escalibure", 5, 4, 6, 3)
# >>> print(epee)
# {
#     "nom": "epee",
#     "degat magique": 0,
#     "degat_physique": 10,
#     "poids": 5,
#     "cout_magique": 0
# }


# Exercice n02 : joueur
# ecrire une fonction (`new_player`) qui cree un personnage. Un personnage est
# constituer de:
# - son nom
# - son type (magicien ou gerrier)
# - ses points de vie (pv)
# - ses points de magique (mana)
# - ses points de force (strenght)
# - son arme que l'on as cree avec `new_weapon`
#
# le personnage devra aussi avoir ses points de vie, magie et force max.
def new_player(name, type, pv, mana, force, weapon):
    return {
        "name": name,
        "type": type,
        "pv": pv,
        "mana": mana,
        "force": force,
        "weapon": weapon
    }


# tests
perso1 = new_player("kevin", "magicien", 100, 50, 20, epee)
perso2 = new_player("ilian", "gerrier", 120, 30, 40, bagette_magique)
# >>> print(perso1)
# {
#     'name': 'kevin',
#     'type': 'magicien',
#     'pv': 100,
#     'mana': 50,
#     'force': 20,
#     'weapon': {
#         'name': 'epee',
#         'physical_domage': 0,
#         'magic_domage': 10,
#         'physical_cost': 5,
#         'magic_cost': 0
#     }
# }

# Exercice n03 : en garde
# ecrire une fonction (`can_attack`) qui prend un joeur en parametre et renvoie
# si il peut attaquer ou non
def can_attack(player):
    weapon = player['weapon']
    if player['mana'] >= weapon['magic_cost'] and player['force'] >= weapon['physical_cost']:
        return True
    else:
        return False


def can_attack(player):
    return player['mana'] >= player['weapon']['magic_cost'] \
        and player['force'] >= player['weapon']['physical_cost']  # le backslash (\) est pour eviter pouvoir sauter une ligne


# tests
print(can_attack(perso1))


# Exercice n04 : attaquer
# ecrire une fonction (`attack`) qui pend 2 joueurs en parametre 1 joueur qui
# attaque et l'autre est la cible.
# la fonction prend l'arme du joueur 1 regarde si il peut l'utiliser et si oui
# attaque le joueur 2 avec celle ci. ne pas oublier de decendre des points de
# mana et de force du joueur
# la fonction revoie si le joueur a attacker ou non
def attack(attacker, target):
    # verifier que l'attaquant peut attaquer
    if can_attack(attacker):
        # si oui attaque (actualiser la mana et les points de force de attaquant
        # et retirer au pv cible lattaque magique et physique de l'arme)
        target['pv'] -= attacker['weapon']['physical_domage'] + attacker['weapon']['magic_domage']
        attacker['mana'] -= attacker['weapon']['magic_cost']
        attacker['force'] -= attacker['weapon']['physical_cost']
        # revoie vrai
        return True
    # si non
    else:
        # revoie faux
        return False

# soit le personnage
# player = {
#     'name': 'kevin',
#     'type': 'magicien',
#     'pv': 100,
#     'mana': 50,
#     'force': 20,
#     'weapon': {
#         'name': 'epee',
#         'physical_domage': 0,
#         'magic_domage': 10,
#         'physical_cost': 5,
#         'magic_cost': 0
#     }
# }
# accedet a  player -> weapon -> physical_cost
# est equivalent a
# player['mana'] = player['mana'] - player['weapon']['magic_cost']

# cible['pv'] = cible['pv'] - player['weapon']['physical_domage'] - player['weapon']['magic_domage']
# est equivalent a:
# cible['pv'] = cible['pv'] - (player['weapon']['physical_domage'] + player['weapon']['magic_domage'])
# est equivalent a:
# cible['pv'] -= (player['weapon']['physical_domage'] + player['weapon']['magic_domage']

print('perso 1', perso1)
print('perso 2', perso2)
print(attack(perso1, perso2))
print('perso 1', perso1)
print('perso 2', perso2)

# Exercice n05 : KO ou OK ?
# ecrire une fonction (`alive`) qui dit si un joueur est en vie ou pas
def alive(player):
    return player['pv'] > 0

# Exerice n06 : repos Zzzz
# lors d'un combat il n'y a pas que des phases d'actions il faut aussi se reposer
# la fonction `rest` regenere 10 points de force et 5 points de mana
def rest(player):
    player['force'] += 10
    player['mana'] += 5

# Exercice n07 : combat 1
# la fonction `fight` prend 2 joueurs en parametre et les faits les se combattre.
# les regles sont simple:
# - c'est du tour par tour
# - le 1ere joueur commence
# - le joueur essaiye d'attaquer, si il peut pas il se repose
# - le combat se finie quand l'un des 2 personnage est KO
#
# a la fin du combat on affiche le gagnant


# Player1 magicien: 100PV 10 force 20 mana
# Player2 gerier: 100PV 10 force 20 mana
# Voulez vous attaquer ou vous deffendre: