import random
print("Number guess game")
ran=random.randint(1,100)
guessednum=None
guesses=0
while guessednum!=ran:
    guessednum=int(input("Guess the number;"))
    guesses+=1
    if guessednum > ran:
        print("You guessed wrong!Enter smaller number")
    else:
        print("You guessed wrong!Enter larger number")
print(f"You guesaed in {guesses}turns")
with open('user.txt','r') as f:
    high=int(f.read())
if guesses<high:
    print("You make new record")
    with open('user.txt','w') as f:
        f.write(guesses)