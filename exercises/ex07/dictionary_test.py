"""Test functions for EX07."""

__author__ = "730471672"

from exercises.ex07.dictionary import count, favorite_colors, invert


def test_sum_invert_use() -> None:
    """Use case for invert."""
    the_dict: dict[str, str] = {}
    assert invert(the_dict) == {}


def test_sum_invert_edge_one() -> None:
    """One edge case for invert."""
    the_dict: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(the_dict) == {"b": "a", "d": "c"}


def test_sum_invert_edge_two() -> None:
    """Another edge case for invert."""
    the_dict: dict[str, str] = {"hello": "world", "what": "is", "up": "?"}
    assert invert(the_dict) == {"world": "hello", "is": "what", "?": "up"}


def test_sum_favorite_colors_edge() -> None:
    """An edge case for favorite colors."""
    the_dict: dict[str, str] = {}
    assert favorite_colors(the_dict) == ""


def test_sum_favorite_colors_use_one() -> None:
    """A use case for favorite colors."""
    the_dict: dict[str, str] = {"bob": "red", "cassidy": "red", "jack": "blue", "dan": "green", "sophie": "blue", "hayden": "red"}
    assert favorite_colors(the_dict) == "red"


def test_sum_favorite_colors_use_two() -> None:
    """Another use case for favorite colors."""
    the_dict: dict[str, str] = {"bob": "red", "cassidy": "red", "jack": "blue", "dan": "green", "sophie": "blue", "hayden": "yellow"}
    assert favorite_colors(the_dict) == "red"


def test_sum_count_edge() -> None:
    """An edge case for count."""
    the_list: list[str] = []
    assert count(the_list) == {}


def test_sum_count_use_one() -> None:
    """A use case for count."""
    the_list: list[str] = ["a", "b", "c", "b", "a"]
    assert count(the_list) == {"a": 2, "b": 2, "c": 1}


def test_sum_count_use_two() -> None:
    """Another use case for count."""
    the_list: list[str] = ["1", "2", "3", "1", "2", "3", "2", "1", "3", "5"]
    assert count(the_list) == {"1": 3, "2": 3, "3": 3, "5": 1}



