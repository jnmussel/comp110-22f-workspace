"""EX05 - `list` Utility Functions."""

__author__ = "730471672"


def only_evens(input: list[int]) -> list[int]:
    """Returns even integers of a list."""
    i: int = 0
    even_list = []
    while i < len(input):
        if input[i] % 2 == 0:
            even_list.append(input[i])
        i += 1
    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Combines two lists."""
    i: int = 0
    final_list = list1
    while i < len(list2):
        final_list.append(list2[i])
        i += 1
    return final_list


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    """Returns a subset between given indices."""
    end_list = []
    if start < 0:
        start = 0
    if end > len(input_list):
        end = len(input_list)
    if len(input_list) == 0:
        return end_list
    if start > len(input_list):
        return end_list
    if end <= 0:
        return end_list
    i: int = start
    while i < end:
        end_list.append(input_list[i])
        i += 1
    return end_list
    
