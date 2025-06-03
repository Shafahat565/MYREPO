import random
def cls():
    print('\n'*50)
def game(you,comp):
    if comp==you:
       return print("Game Tie")
    elif comp=='s' and you=='w' or comp=='w' and you=='g' or comp=='g' and you=='s':
        return print("You lose")
    elif comp=='s' and you=='g' or comp=='w' and you=='s' or comp=='g' and you=='w':
        return print("You won")
over=1        
while over >0 :
    ran=random.randint(1,3)
    if ran==1 :
       comp='s'
    elif ran==2 :
       comp='w'
    elif ran==3 :
        comp='g'
    ran=random.randint(1,3)
    if ran==1 :
       comp='s'
    elif ran==2 :
       comp='w'
    elif ran==3 :
        comp='g'    
    print("Hello! Lets play a Game Water,Snake ,Gun")    
    print("Computer choosed")
    you=input("You turn:\n Enter (g) for gun \n Enter (w) for water \n Enter (s) for snake\n::")
    print(f"You chose {you}")
    print(f"Comp chose {comp}")
    game(you,comp)
    over=int(input("Enter zero to end game \nEnter number greater than zero to play again"))
    cls()