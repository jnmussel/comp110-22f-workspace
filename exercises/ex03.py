"""EX03- Structured Wordle"""

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

    

        

