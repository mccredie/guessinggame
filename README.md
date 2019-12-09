# Guessing game

My son wanted me to show him how to program. We started playing with a
guessing game in python. Then he wanted me to give it a gui. So I gave it a
gui. Then I wanted to use a reducer pattern to see if I could use the same
logic for the gui and the cli.

## Notes on teaching my son

The file `hello.py` contains our first exercise. It started as a basic hello
world.

We added an input, and had the user input their name, and said hello to them. This enabled us to introduce the concept of variables and string formatting.

This had the side effect of me needing to discuss types with him, since you
have to cast the input to an int.

Third we implemented the guessing game, but we didn't use a loop, we just
copied the same code several times for each guess. This introduced the
concept of a conditional. I also had to `import random`.

Fourth we introduced a loop and removed all of the duplicate code.

