"""EX02 One Shot Wordle."""

__author__ = "730471672"
secret: str = str("python")
guess: str = str(input("What is your 6 letter guess? "))
while len(guess) != 6:
    guess: str = str(input("That was not 6 letters! Try again: "))

if guess == secret:
    outcome: str = "Woo! You got it!"
else:
    outcome: str = "Not quite. Play again soon!"

i: int = 0
color: str = ""

while i < len(guess):
    if guess[i] == secret[i]:
        color = color + str("\U0001F7E9")
    else:
        alt: bool = False
        j: int = 0
        while alt is not True and j < len(secret):
            if secret[j] == guess[i]:
                alt: bool = True
            else:
                j = j + 1
        if alt is True:
            color = color + str("\U0001F7E8")
        else:
            color = color + str("\U00002B1C")
    i = i + 1

print(color)
print(outcome)