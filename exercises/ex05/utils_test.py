"""Utils test for EX05."""

__author__ = "730471672"

from exercises.ex05.utils import only_evens, concat, sub

def test_sum_only_evens_empty() -> None:
    """Edge case for only evens."""
    input = []
    assert only_evens(input) == []


def test_sum_only_evens_one_even() -> None:
    """Use case for only evens with one even number."""
    input: list[int] = [1, 2, 3]
    assert only_evens(input) == [2]


def test_sum_only_evens_negative() -> None:
    """Use case for only evens with negative numbers."""
    input: list[int] = [-3, -2, -1, 0, 1, 2, 3]
    assert only_evens(input) == [-2, 0, 2]


def test_sum_concat_empty() -> None:
    """Edge case for concat function."""
    list1 = []
    list2 = []
    assert concat(list1, list2) == []


def test_sum_concat_many_items() -> None:
    """Use case for concat function."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_sum_concat_many_items_again() -> None:
    """Another use case for concat function."""
    list1: list[int] = [-5, -2, 1, 4]
    list2: list[int] = [2, -9, 3]
    assert concat(list1, list2) == [-5, -2, 1, 4, 2, -9, 3]


def test_sum_sub_empty() -> None:
    """Edge case for sub function (empty list)."""
    input_list = []
    start = 0
    end = 4
    assert sub(input_list, 0, 4) == []


def test_sum_sub_full() -> None:
    """Use case for sub function."""
    input_list: list[int] = [0, 1, 2, 3, 4, 5]
    start = 1
    end = 3
    assert sub(input_list, 1, 3) == [1, 2]


def test_sum_sub_full_again() -> None:
    """Another use case for sub function."""
    input_list: list[int] = [3, 4, 5, 6, 7, 8]
    start = 2
    end = 8
    assert sub(input_list, 2, 8) == [5, 6, 7, 8]