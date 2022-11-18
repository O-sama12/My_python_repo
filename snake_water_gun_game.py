# Make sure you've check my readme file, if not then go & check it
import random as rd
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
                return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
                return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
                return True                        
randno = rd.randint(1,3)
print("Computer's turn: Snake(s) Water(w) or Gun(g): ")
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
else:
    comp = 'g'
you = input("Player's Turn: Snake(s) Water(w) or Gun(g): ")    
a = gameWin(comp, you)
print(f'Computer chose {comp}')
print(f'You chose {you}')
if a == None:
    print("The game's tie")
elif a:
    print('You Win')
else:
    print('Computer win')        