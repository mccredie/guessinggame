import sys
import random

# Get a random number (int) between 1 and 100
number = random.randint(1, 100)
guesses_remaining = 5

print("I'm thinking of a number between 1 and 100, can you guess it?")

while guesses_remaining > 0:
    print(f"You have {guesses_remaining} tries remaining.")
    print("What is your guess?")

    # Get a guess and turn it into a number (int)
    guess = int(input())

    if guess == number:
        print("Oh my gosh what a guess! You win!")
        # Exit the program right away
        sys.exit()

    if guess < number:
        print("Oops, too low.")

    if guess > number:
        print("Nope, too high.")

    guesses_remaining = guesses_remaining - 1