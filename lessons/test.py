"""testing stuff"""

def subset(input_dict: dict[int, str], input_list: list[int]) -> dict[int, str]:
    output: dict[int, str] = {}
    for item in input_list:
        if item in input_dict:
            output[item] = input_dict[item]
    return output

from typing import Union

def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result

print(add(110.0))
print(add(110.0, "100.0"))
print()