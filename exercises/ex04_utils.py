"""First list exercise for COMP110. """

__author__ = "730471672"

def all(a: list[int], b: int) -> bool:
    """all should return a bool indicating whether or not all the ints in the list are the same as the given int."""
    i: int = 0
    var1: bool = True
    while i < len(a) and var1 is True:
        if a[i] != b:
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
    while k < len(input):
        if input[k + 1] > input[k]:
            var2 = input[k + 1]
    k = k + 1
    return var2
    
def is_equal(c: list[int], d: list[int]) -> bool:
    """Checks for identical indices."""
    if len(c) > len(d):
        var3: int = len(d)
    else:
        var3: int = len(c)
    j: int = 0
    var4: bool = True
    while j < var3:
        if c[j] != d[j]:
            var4 = False
    j = j + 1
    return var4
        
    