import sys
import random

# Get a random number (int) between 1 and 100
number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100, can you guess it?")
print("I'll give you 5 tries")
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

print("Try again. You have 4 guesses remaining.")
print("What is your guess?")
guess = int(input())

if guess == number:
    print("Oh my gosh what a guess! You win!")
    sys.exit()

if guess < number:
    print("Oops, too low.")

if guess > number:
    print("Nope, too high.")

print("Try again. You have 3 guesses remaining.")
print("What is your guess?")
guess = int(input())

if guess == number:
    print("Oh my gosh what a guess! You win!")
    sys.exit()

if guess < number:
    print("Oops, too low.")

if guess > number:
    print("Nope, too high.")

print("Try again. You have 2 guesses remaining.")
print("What is your guess?")
guess = int(input())

if guess == number:
    print("Oh my gosh what a guess! You win!")
    sys.exit()

if guess < number:
    print("Oops, too low.")

if guess > number:
    print("Nope, too high.")

print("Try again. You have 1 guesses remaining.")
print("What is your guess?")
guess = int(input())

if guess == number:
    print("Oh my gosh what a guess! You win!")
    sys.exit()

if guess < number:
    print("Oops, too low.")

if guess > number:
    print("Nope, too high.")

print("Game over. You lose!")