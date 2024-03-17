import random
from random import choice

set_sujet = ['il', 'ce mec', 'le rideau', 'une toupie', "clement", "Ice Murder", " Yondu"]
set_verbe = ['a', 'aime', 'saute', 'parle', 'tremble']
set_complement = ["car c'est bon pour la santé", "pour oublier", "de haut en bas", "vraiment", 'de terreur', 'comme si ']


maj = random.choice(set_sujet)
maj = maj[0].upper() + maj[1:]
verbe = random.choice(set_verbe)
complement = random.choice(set_complement)

phrase = maj,  verbe, complement,"."
print(" ".join(phrase))


#urllib.request.urlretrieve(remote,dst)