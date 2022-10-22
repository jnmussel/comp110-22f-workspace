"""testing stuff"""

def subset(input_dict: dict[int, str], input_list: list[int]) -> dict[int, str]:
    output: dict[int, str] = {}
    for item in input_list:
        if item in input_dict:
            output[item] = input_dict[item]
    return output
