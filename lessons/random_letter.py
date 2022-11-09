"""Returns a random letter."""


from random import randint
param: int = randint(0, 25)

def random_letter(x: int) -> str:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[x]

print(f"The randomly generated letter is: {random_letter(param)}")

