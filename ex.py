
player = input('pierre (pi) papier (pa)  ciseaux(c)?')
player2 = input('pierre (pi) papier (pa)  ciseaux(c)?')
if player == 'pi':
    print('O', end=' ')

elif player == 'pa':
    print('___', end=' ')

elif player == 'c':
    print('>8', end=' ')

else:
    print('??')

print('vs', end=' ')

chosen = randint(1, 3)

if chosen == 1:
    player2 = 'r'
    print('O')

elif chosen == 2:
    player2 = 'pa'
    print('___')

else:
    player2 = 's'
    print('>8')

if player == player2:
    print('0 à 0')

elif player == 'pi' and player2 == 'c':
    print('Player wins!')

elif player == 'pi' and player2 == 'pa':
    print('Computer wins!')

elif player == 'pa' and player2 == 'pi':
    print('Player wins!')

elif player == 'pa' and player2 == 'c':
    print('Computer wins!')

elif player == 'c' and player2 == 'pa':
    print('Player wins!')

elif player == "c" and player2 == 'pi':
    print('Computer wins!')

else:
    print('Huh?')

