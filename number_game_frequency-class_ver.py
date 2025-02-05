from random import random

import random
#random target generation
#guessing algorithm
#feedback mechanism - number of guesses
#data collection - simulate games
#data analysis - compute average
#data presentation - sort and print results

def binary_search_guess(target):
#guessing algorithm




def simulate_games(num_games):
#simulate the guessing game for a given number of games.
# Returns a dictionary with target numbers as keys and a tuple of total guesses and count of games as values.
#This function simulates the guessing game for a given number of games and keeps track of the total number of guesses and the count of games for each target number.
    results = {0: (0, 0)for n in range(1,101)}
    print(type(results))


    for _ in range(num_games): # Use _ as a throwaway variable since we don't need the loop index
        target = random.randint(1, 100) # choose a random target number between 1 and 100
        print("Target is ", target)
        num_guesses = binary_search_guess(target) # run the guessing algorithm and get the number of guesses
        total_guesses, games = results[target]
        results[target] = (total_guesses + num_guesses, games + 1)
        print(results)

    return results
def main():
    #The main function runs the simulation, computes averages, sorts them for easier review and prints the results.
    num_games = 1000
    results = simulate_games(num_games)