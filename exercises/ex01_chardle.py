"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730471672"
fiveletterword: str = str(input("Enter a 5 letter word: "))
if len(fiveletterword) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    singleletter: str = str(input("Enter a single character: "))
    if len(singleletter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print("Searching for " + singleletter + " in " + fiveletterword)

total: int = int(0)   

if singleletter == fiveletterword[0]:
    print(singleletter + " found at index 0")
    total = total + 1
if singleletter == fiveletterword[1]:
    print(singleletter + " found at index 1")
    total = total + 1
if singleletter == fiveletterword[2]:
    print(singleletter + " found at index 2")
    total = total + 1
if singleletter == fiveletterword[3]:
    print(singleletter + " found at index 3")
    total = total + 1
if singleletter == fiveletterword[4]:
    print(singleletter + " found at index 4")
    total = total + 1

if total > int(1):
    print(str(total) + " instances of " + singleletter + " found in " + fiveletterword)
else:
    if total == 1:
        print(str(total) + " instance of " + singleletter + " found in " + fiveletterword)
    else:
        if total == 0:
            print("No instances of " + singleletter + " found in " + fiveletterword)