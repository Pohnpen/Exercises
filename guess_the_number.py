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

# PR: Very good!
x = random.randint(1, 100)

for i in range(0, T):
    # TODO: Would be nice to know how many guess left. Something like 3 guesses left. Use an f-string
    print("Try to guess the random number")
    guess = int(input())
    if x == guess:
        print("Bravo")
    else:
        # TODO: "Sorry, try again"
        print("Sorry")

# TODO: If the loop exits display a message, that the user has lost the game, since no more guesses are left