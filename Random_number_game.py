#guess the number game
# create a random number between 1 and 100
#ask the user to guess the number
#tell the user if the number is higher or lower than the guess
#tell the user if they are correct
#keep asking user to guess until they get it right
import random
number = random.randint(1,100)
guess = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    else:
        print("Correct")