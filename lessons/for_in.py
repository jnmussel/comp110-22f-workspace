"""An example of for in syntax."""

names: list[str] = ["John", "Bob", "Beyonce", "Biden"]

# Example of iterating through names using a while loop.
print("while loop output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for..in loop is the same as the while loop above.
print("for..in output:")
for name in names:
    print(name)

