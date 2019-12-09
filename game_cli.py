import math
from engine import init, guess


max_guess = 100
guesses = math.floor(math.log2(max_guess))

def main():
    game_state = init(max_guess, guesses)

    while not game_state.game_over:
        game_state = guess(game_state, prompt(game_state))

    end_game(game_state)


def prompt(game_state):
    print(
        "I'm thinking of a number between "
        f"{game_state.lower_bound+1} and {game_state.upper_bound-1}"
    )
    print(f"you have {game_state.tries_remaining} tries remaining.")
    number = None
    while number is None:
        try:
            number = int(input("What is your guess?"))
        except ValueError:
            print("Invalid input. Please enter a number.")
    return number

def end_game(game_state):
    if game_state.player_won:
        print("Congratulations, you won!")
    else:
        print("You lose, too bad.")

if __name__ == "__main__":
    main()