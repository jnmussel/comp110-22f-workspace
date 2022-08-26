"""random stuff"""

a: str = "a"
b: str = "b"
c: str = b

b = a
a = c

print(a)
print(b)
print(c)
