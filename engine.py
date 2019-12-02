
import random
from dataclasses import dataclass, replace


@dataclass
class GameState:
    number: int
    max_guess: int
    lower_bound: int
    upper_bound: int
    tries_remaining: int
    player_won: bool = False

    @property
    def game_over(self):
        return self.player_won or self.tries_remaining <= 0


# reducers
def init(max_guess, tries_remaining):
    return GameState(
        number=random.randint(1, max_guess),
        max_guess=max_guess,
        lower_bound=0,
        upper_bound=(max_guess + 1),
        tries_remaining=tries_remaining
    )

def guess(state, number):
    if state.game_over:
        return state
    state = replace(state, tries_remaining=state.tries_remaining-1)
    if number == state.number:
        state = replace(state, player_won=True)
    elif number < state.number:
        state = replace(state, lower_bound=number)
    elif number > state.number:
        state = replace(state, upper_bound=number)
    return state

