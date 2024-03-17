# exercice 1
# ecrire une fonction qui fait la somme de tous les nombres d'une liste
# exemple
# sum_list([1, 2, 3, 4]) => 10
l = [1, 2, 3, 4]
def sum_list(l):
    s = 0
    for i in l:
        s = s +i
    return s
print(sum_list(l))

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True    

print(is_sorted(l)) 
# ecrire une fonction qui retourne si une liste est trié par ordre croissant
# exemple
# is_sorted([1, 2, 3, 4]) => true
# is_sorted([4, 3, 2, 1]) => false

# exerice 3
# double doubler la valeur de chaque element d'une liste
# exemple:
# l = [1,2,3,4,5]
# double(l)
# l => [2, 4, 6, 8, 10]