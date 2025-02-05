#guess the number game
#chooses a random number between 1 and 100
#ask the user to guess the number
#tells the user if the number is higher or lower than the guess
#tells the user if they are correct
#keep asking user to guess until they get it right
import random
import os

# Function to read previous guesses from file
def read_previous_guesses(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            guesses = file.readlines()
            return [int(guess.strip()) for guess in guesses]
    else:
        return []

# Function to write guesses to file
def write_guesses(file_path, guesses):
    with open(file_path, "w") as file:
        for guess in guesses:
            file.write(f"{guess}\n")

file_path = "guesses.txt"
number = random.randint(1, 100)
guess = 0
guesses = 0
guess_list = read_previous_guesses(file_path)  # Read previous guesses

print("Previous guesses:", guess_list)

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    else:
        print("Correct")
    guesses += 1
    guess_list.append(guess)
    write_guesses(file_path, guess_list)  # Write guesses to file after each guess

print("You took", guesses, "guesses")
print("Your guesses were:", guess_list)