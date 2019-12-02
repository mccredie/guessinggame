import math
import random
import tkinter as tk


def main():
    root = tk.Tk()
    GameContainer(root, 400, 10).pack() 
    root.mainloop()


class GameContainer(tk.Frame):
    def __init__(self, root, max_guess, tries):
        super().__init__(root)
        self.max_guess = max_guess
        self.tries = tries
        self._start()

    def _start(self):
        guess = random.randint(1, self.max_guess)
        self.game = Game(self, self.max_guess, self.tries, guess, self.handle_restart)
        self.game.pack()

    def handle_restart(self):
        self.game.destroy()
        self._start()


class Game(tk.Frame):
    def __init__(self, root, max_guess, tries, number, on_restart):
        super().__init__(root)
        self.max_guess = max_guess
        self.tries = tries
        self.number = number
        self.on_restart = on_restart
        self._start()

    def _start(self):
        self.display = TriesDisplay(self, self.tries)
        self.display.pack()
        self.guess_input = GuessInput(self, self.max_guess, self.handle_guess)
        #self.guess_input = GuessInputCanvas(self, self.max_guess, self.handle_guess)
        self.guess_input.pack()

    def handle_guess(self, guess):
        self.tries -= 1
        self.display.set_remaining(self.tries)
        if guess == self.number:
            self.guess_input.set_bounds(upper=guess, lower=guess)
            self._game_over(win=True)
        else:
            if guess < self.number:
                self.guess_input.set_bounds(lower=guess)
            elif guess > self.number:
                self.guess_input.set_bounds(upper=guess)
            if self.tries == 0:
                self._game_over(win=False)
    
    def _game_over(self, win):
        self.guess_input.destroy()
        del self.guess_input
        self.result = Result(self, win, self.on_restart)
        self.result.pack()


class TriesDisplay(tk.Frame):
    def __init__(self, root, tries):
        super().__init__(root)
        self.tries = tries
        self.remaining = tries
        self.label = tk.Label(self, text=self._get_text())
        self.label.pack(fill=tk.BOTH, expand=True)

    def set_remaining(self, remaining):
        self.remaining = remaining
        self.label.config(text=self._get_text())

    def _get_text(self):
        return f"Guess my number: {self.remaining} of {self.tries} tries remaining"


class GuessInput(tk.Frame):
    def __init__(self, root, max_guess, on_guess):
        super().__init__(root)
        buttons = []
        self.upper_bound = max_guess + 1
        self.lower_bound = 0

        side_len = math.ceil(math.sqrt(max_guess))
        for i in range(max_guess):
            button = GuessButton(self, i+1, on_guess)
            button.grid(row=i//side_len, column=i%side_len)
            buttons.append(button)
        self.buttons = buttons

    def set_bounds(self, upper=None, lower=None):
        if upper is not None:
            self.upper_bound = upper
        if lower is not None:
            self.lower_bound = lower
        for button in self.buttons:
            if button.number <= self.lower_bound or button.number >= self.upper_bound:
                button.disable()

class GuessInputCanvas(tk.Frame):
    def __init__(self, root, max_guess, on_guess):
        super().__init__(root)
        self.max_guess = max_guess
        self.upper_bound = max_guess + 1
        self.lower_bound = 0
        self.on_guess = on_guess

        self.label = tk.Label(self, text="Sup")
        self.label.pack()
        self.canvas = tk.Canvas(self, width=200, height=20, bd=0, highlightthickness=0)
        self.canvas.bind('<Motion>', self._move)
        self.canvas.bind('<Button-1>', self._click)
        self.upper_bound_rect = self.canvas.create_rectangle(200, 0, 200, 200, fill="red")
        self.lower_bound_rect = self.canvas.create_rectangle(0, 0, 0, 0, fill="red")
        self.canvas.pack()
    
    def _move(self, event):
        guess = 1 + int(self.max_guess * (event.x / 200))
        self.label.config(text=f"Guess? {guess}")
    
    def _click(self, event):
        guess = 1 + int(self.max_guess * (event.x / 200))
        self.label.config(text=f"Guessed: {guess}")
        self.on_guess(guess)


    def set_bounds(self, upper=None, lower=None):
        if upper is not None:
            self.canvas.coords(self.upper_bound_rect, (upper / self.max_guess) * 200, 0, 200, 20)
            self.upper_bound = upper
        if lower is not None:
            self.canvas.coords(self.lower_bound_rect, 0, 0, (lower /self.max_guess) * 200, 20)
            self.lower_bound = lower


class GuessButton(tk.Button):
    def __init__(self, root, number, on_guess):
        super().__init__(root, text=number, command=self.handle_guess)
        self.number = number
        self.on_guess = on_guess
        self.enabled = True

    def handle_guess(self):
        self.on_guess(self.number)

    def disable(self):
        if self.enabled:
            self.config(state=tk.DISABLED)
            self.enabled = False


class Result(tk.Frame):
    font = 'Sans Serif', 240

    def __init__(self, root, win, on_play_again):
        super().__init__(root)
        if win: 
            self.label = tk.Label(
                self, text="You Win!", font=self.font, fg='green')
        else:
            self.label = tk.Label(
                self, text="You Lose!", font=self.font, fg='red')
        self.label.pack()
        self.button = tk.Button(self, text="Play Again", command=on_play_again)
        self.button.pack(expand=True, fill=tk.X)


if __name__ == "__main__":
    main()