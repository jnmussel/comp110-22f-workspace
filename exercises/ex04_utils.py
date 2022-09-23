"""First list exercise for COMP110."""

__author__ = "730471672"


def all(list1: list[int], int1: int) -> bool:
    """All should return a bool indicating whether or not all the ints in the list are the same as the given int."""
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
    i: int = 0
    curr_max: int = input[0]
    while i < len(input):
        if input[i] > curr_max:
            curr_max = input[i]
        i = i + 1
    return curr_max
    

def is_equal(list2: list[int], list3: list[int]) -> bool:
    """Checks for identical indices."""
    i: int = 0
    if len(list2) != len(list3):
        return False
    while i < len(list2):
        if list2[i] != list3[i]:
            return False
        i = i + 1
    return True
    