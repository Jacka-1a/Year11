#guess the number game
# create a random number between 1 and 100
#ask the user to guess the number
#tell the user if the number is higher or lower than the guess
#tell the user if they are correct
#keep asking user to guess until they get it right
import random
number = random.randint(1,100)
guess = 0
guesses = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    # creates a list and puts player guesses in it.
    guess_list = []
    if guess > number:
        print("Lower")
        guesses += 1
    #adds player input into list
        guess_list.append(guess)
    elif guess < number:
        print("Higher")
        guesses += 1
        guess_list.append(guess)
    else:
        print("Correct")
        guesses += 1
        guess_list.append(guess)
# saves the number of guesses and prints it
print("You took", guesses, "guesses")
print ("Your guesses were: ", guess_list)