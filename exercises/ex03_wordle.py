"""EX03- Structured Wordle."""

__author__ = "730471672"


def contains_char(word: str, letter: str) -> bool:
    """Verifies if a word contains a given letter. """
    assert len(letter) == 1
    i: int = 0
    check: bool = False
    while i < len(word) and check is not True:
        if str(letter) == str(word[i]):
            check = True
        i = i + 1
    return check


def emojified(guess: str, secret: str) -> str:
    """Function for colored boxes. """
    assert len(guess) == len(secret)
    j: int = 0
    color: str = ""
    while j < len(guess):
        if guess[j] == secret[j]:
            color = color + str("\U0001F7E9")
        else:
            if contains_char(secret, guess[j]) is True:
                color = color + str("\U0001F7E8")
            else:
                color = color + str("\U00002B1C")
        j = j + 1
    return color


def input_guess(length: int) -> str:
    """Makes sure user inputs word with right amount of letters. """
    hey: str = input("Enter a " + str(length) +  " character word: ")
    while len(hey) != length:
        hey: str = input("That wasn't " + str(length) + " chars! Try again : ")
    return hey
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    playing: bool = True
    while turn <= 6 and playing is True:
        print("=== Turn " + str(turn) + "/6 ===")
        gameguess: str = input_guess(5)
        gsecret: str = "codes"
        if gameguess == gsecret:
            print(emojified(gameguess, gsecret))
            print("You won in " + str(turn) + "/6 turns!")
            playing = False
        else:
            print(emojified(gameguess, gsecret))
        turn = turn + 1
    if turn > 6 and playing is True:
        print("X/6 - Sorry, try again tomorrow!")
        playing = False


if __name__ == "__main__":
    main()
