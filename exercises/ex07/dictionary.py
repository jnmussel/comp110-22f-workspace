"""EX07 Dictionaries."""

__author__ = "730471672"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of a dictionary."""
    new_dict: dict[str, str] = {}
    for item in input_dict:
        if input_dict[item] in new_dict:
            raise KeyError("2 values cannot be the same!")
        new_dict[input_dict[item]] = item
    return new_dict


def favorite_colors(input_dict: dict[str, str]) -> str:
    """Returns the most popular color in a dict."""
    max: int = 1
    fav_color: str = ""
    color_dict: dict[str, int] = {}
    for item in input_dict:
        if input_dict[item] in color_dict:
            color_dict[input_dict[item]] += 1
        else:
            color_dict[input_dict[item]] = 1
    
    for thing in color_dict:
        if color_dict[thing] > max:
            max = color_dict[thing]
            fav_color = thing
    return fav_color
    

def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dict of counting number of occurrences of a str in a list."""
    the_dict: dict[str, int] = {}
    for item in input_list:
        if item in the_dict:
            the_dict[item] += 1
        else:
            the_dict[item] = 1
    return the_dict
