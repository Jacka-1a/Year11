#guess the number game
# create a random number between 1 and 100
#ask the user to guess the number
#tell the user if the number is higher or lower than the guess
#tell the user if they are correct
#keep asking user to guess until they get it right
import random
from contextlib import nullcontext
from mimetypes import guess_extension

number = random.randint(1,100)
guess = 0
guesses = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == nullcontext
    if guess > number:
        print("Lower")
        guesses += 1
    elif guess < number:
        print("Higher")
        guesses += 1
    else:
        print("Correct")
        guesses += 1
# saves the number of guesses and prints it
print("You took", guesses, "guesses")