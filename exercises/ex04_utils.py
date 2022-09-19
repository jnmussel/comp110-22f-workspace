"""First list exercise for COMP110."""

__author__ = "730471672"


def all(list1: list[int], int1: int) -> bool:
    """all should return a bool indicating whether or not all the ints in the list are the same as the given int."""
    i: int = 0
    var1: bool = True
    if len(list1) == 0:
        var1: bool = False
    while i < len(list1) and var1 is True:
        if list1[i] != int1:
            var1 = False
        else:
            i = i + 1
    return var1


def max(input: list[int]) -> int:
    """Finds maximum value of a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    k: int = 0
    var2: int = input[0]
    while k < len(input) - 1:
        if input[k + 1] > input[k]:
            var2 = input[k + 1]
    k = k + 1
    return var2
    

def is_equal(list2: list[int], list3: list[int]) -> bool:
    """Checks for identical indices."""
    if len(list2) > len(list3):
        var3: int = len(list3) - 1
    elif len(list2) == len(list3):
        var3: int = len(list2) - 1
    else:
        var3: int = len(list2) - 1
    j: int = 0
    var4: bool = True
    while j < var3:
        if list2[j] != list3[j]:
            var4 = False
    j = j + 1
    return var4
        
    