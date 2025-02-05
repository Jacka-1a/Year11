import subprocess
import random
import time


# Function to generate a random number between lower and upper bounds
def generate_random_input(lower, upper):
    return random.randint(lower, upper)


# Initialize bounds and found flag
lower_bound = 1
upper_bound = 100
found = False

# Loop until the correct number is found
while not found:
    # Generate a random guess
    guess = generate_random_input(lower_bound, upper_bound)
    print(f"Auto guess: {guess}")

    # Run the guess game and pass the guess as input
    process = subprocess.Popen(['python', 'Random_number_game.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)

    # Communicate the guess to the game and capture output
    out, err = process.communicate(input=str(guess))

    # Print the result from the game
    print(out)

    # Check the response from the game to adjust bounds or determine if found
    if "Lower" in out:
        upper_bound = guess - 1
    elif "Higher" in out:
        lower_bound = guess + 1
    elif "Correct" in out:
        found = True

    # Add a short delay to avoid rapid looping
    time.sleep(1)
