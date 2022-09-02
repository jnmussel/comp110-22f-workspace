"""EX02 One Shot Wordle"""

__author__ = "730471672"
secret: str = str("python")
guess: str = str(input("What is your 6 letter guess? "))
while len(guess) != 6:
    guess: str = str(input("That was not 6 letters! Try again: "))

if guess == secret:
    outcome: str = "Woo! You got it!"
else:
    outcome: str = "Not quite. Play again soon!"

if guess[0] == str("p"):
    first: str = str("\U0001F7E9")
if guess [1] == str("p"):
    first: str = str("\U0001F7E8")
if guess [2] == str("p"):
    first: str = str("\U0001F7E8")
if guess [3] == str("p"):
    first: str = str("\U0001F7E8")
if guess [4] == str("p"):
    first: str = str("\U0001F7E8")
if guess [5] == str("p"):
    first: str = str("\U0001F7E8")
else:
    first: str = str("\U00002B1C")

if guess[1] == str("y"):
    second: str = str("\U0001F7E9")
if guess [0] == str("y"):
    second: str = str("\U0001F7E8")
if guess [2] == str("y"):
    second: str = str("\U0001F7E8")
if guess [3] == str("y"):
    second: str = str("\U0001F7E8")
if guess [4] == str("y"):
    second: str = str("\U0001F7E8")
if guess [5] == str("y"):
    second: str = str("\U0001F7E8")
else:
    second: str = str("\U00002B1C")

if guess[2] == str("t"):
    third: str = str("\U0001F7E9")
if guess [0] == str("t"):
    third: str = str("\U0001F7E8")
if guess [1] == str("t"):
    third: str = str("\U0001F7E8")
if guess [3] == str("t"):
    third: str = str("\U0001F7E8")
if guess [4] == str("t"):
    third: str = str("\U0001F7E8")
if guess [5] == str("t"):
    third: str = str("\U0001F7E8")
else:
    third: str = str("\U00002B1C")

if guess[3] == str("h"):
    fourth: str = str("\U0001F7E9")
if guess [1] == str("h"):
    fourth: str = str("\U0001F7E8")
if guess [2] == str("h"):
    fourth: str = str("\U0001F7E8")
if guess [0] == str("h"):
    fourth: str = str("\U0001F7E8")
if guess [4] == str("h"):
    fourth: str = str("\U0001F7E8")
if guess [5] == str("h"):
    fourth: str = str("\U0001F7E8")
else:
    fourth: str = str("\U00002B1C")

if guess[4] == str("o"):
    fiftht: str = str("\U0001F7E9")
if guess [1] == str("o"):
    fifth: str = str("\U0001F7E8")
if guess [2] == str("o"):
    fifth: str = str("\U0001F7E8")
if guess [3] == str("o"):
    fifth: str = str("\U0001F7E8")
if guess [0] == str("o"):
    fifth: str = str("\U0001F7E8")
if guess [5] == str("o"):
    fifth: str = str("\U0001F7E8")
else:
    fifth: str = str("\U00002B1C")

if guess[5] == str("n"):
    sixth: str = str("\U0001F7E9")
if guess [1] == str("n"):
    sixth: str = str("\U0001F7E8")
if guess [2] == str("n"):
    sixth: str = str("\U0001F7E8")
if guess [3] == str("n"):
    sixth: str = str("\U0001F7E8")
if guess [4] == str("n"):
    sixth: str = str("\U0001F7E8")
if guess [0] == str("n"):
    sixth: str = str("\U0001F7E8")
else:
    sixth: str = str("\U00002B1C")

print(first + second + third + fourth + fifth + sixth)
print(outcome)