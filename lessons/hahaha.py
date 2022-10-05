"""Random docstring."""


thelist: list[str] = ["FLORIDA", "NOTRE DAME", "VIRGINIA TECH", "PITTSBURGH", "GEORGIA TECH", "NC STATE"]

from random import randint

print(thelist[randint(0, 5)])