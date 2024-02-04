# Let's write a program where the user has T trials to guess the a random number between min_n and max_n.
# If the user has correctly guessed the user wins, otherwise the user looses.

"""
Improve
if T == 9 and ...:
    print ("last chance")
if T == 10 and ...:

"""
import random

T = 10
MIN_N = 1
MAX_N = 100
x = random.randint(1, 100)
# create the random number

for i in range(0, T):
    print("Try to guess the random number")
    guess = int(input())
    if x == guess:
        print("Bravo")
    else:
        print("Sorry")

    # check if the guess is == number
