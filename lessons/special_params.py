"""Examples of optional parameters and Union types."""

from typing import Union

def hello(name: Union[str, int] = "World") -> str:
    """A delightful greeting"""
    greeting: str = "Hello, " + name
    return greeting

# Single arguments
print(hello("Sally"))

# No arguments!
print(hello())

# int argument works too!
print(hello(110))