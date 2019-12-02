import math
import random
import tkinter as tk

from engine import init, guess


def main():
    root = tk.Tk()
    game = GameContainer(root, 100, 6)
    game.pack()
    game.handle_restart()
    root.mainloop()

class GameContainer(tk.Frame):
    def __init__(self, root, max_guess, tries):
        super().__init__(root)
        self.max_guess = max_guess
        self.tries = tries
        self.game = Game(self, max_guess, tries, self.handle_guess, self.handle_restart)
        self.game.pack()

    def handle_guess(self, number):
        self.state = guess(self.state, number)
        self._update_state()

    def handle_restart(self):
        self.state = init(self.max_guess, self.tries)
        self._update_state()
    
    def _update_state(self):
        self.game.update_state(
            self.state.tries_remaining, 
            self.state.lower_bound,
            self.state.upper_bound,
            self.state.game_over,
            self.state.player_won)

class Game(tk.Frame):
    def __init__(self, root, max_guess, tries, on_guess, on_restart):
        super().__init__(root)
        self.display = TriesDisplay(self, tries)
        self.display.pack()
        self.guess_input = GuessInput(self, max_guess, on_guess)
        self.guess_input.pack()
        self.result = Result(self, on_restart)
    
    def update_state(self, tries, lower_bound, upper_bound, game_over, player_won):
        self.guess_input.update_state(lower_bound, upper_bound)
        self.display.update_state(tries)
        self.result.update_state(player_won)

        if game_over:
            self.guess_input.pack_forget()
            self.result.pack()
        else:
            self.guess_input.pack()
            self.result.pack_forget()

class TriesDisplay(tk.Frame):
    def __init__(self, root, tries):
        super().__init__(root)
        self.tries = tries
        self.label = tk.Label(self)
        self.label.pack(fill=tk.BOTH, expand=True)

    def update_state(self, remaining):
        self.label.config(text=self._get_text(remaining))

    def _get_text(self, remaining):
        return f"Guess my number: {remaining} of {self.tries} tries remaining"

class GuessInput(tk.Frame):
    def __init__(self, root, max_guess, on_guess):
        super().__init__(root)

        side_len = math.ceil(math.sqrt(max_guess))
        buttons = [
            GuessButton(self, i, on_guess)
            for i in range(1, max_guess + 1)
        ]
        for i, button in enumerate(buttons):
            button.grid(row=i//side_len, column=i%side_len)

        self.buttons = buttons

    def update_state(self, lower, upper):
        for i, button in enumerate(self.buttons, 1):
            enabled = lower < i < upper
            button.update_state(enabled)

class GuessButton(tk.Button):
    def __init__(self, root, number, on_guess):
        super().__init__(root, text=number, command=self.handle_guess)
        self.number = number
        self.on_guess = on_guess

    def handle_guess(self):
        self.on_guess(self.number)

    def update_state(self, enabled):
        state = tk.ACTIVE if enabled else tk.DISABLED
        self.config(state=state)

class Result(tk.Frame):
    font = 'Sans Serif', 240

    def __init__(self, root, on_play_again):
        super().__init__(root)
        self.label = tk.Label(self, font=self.font)
        self.label.pack()
        self.button = tk.Button(self, text="Play Again", command=on_play_again)
        self.button.pack(expand=True, fill=tk.X)

    def update_state(self, player_won):
        if player_won: 
            self.label.config(text="You Win!", fg='green')
        else:
            self.label.config(text="You Lose!", fg='red')


if __name__ == "__main__":
    main()