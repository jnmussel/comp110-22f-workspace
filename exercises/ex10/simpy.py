"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730471672"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Constructor."""
        self.values = values

    def __repr__(self) -> str:
        """Repr for printing."""
        print(f"Simpy({str(self.values)})")

    def fill(self, the_float: float, the_int: int) -> None:
        """Fills a list with a specific number of repeating values."""
        i: int = 0
        while i < the_int:
            self.values.append(the_float)
            i += 1
    
    def arange(self, start: int, stop: int, step: float) -> None:
        """Fills in a list with a start, stop, and step."""
        assert step != 0
        while start < stop:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Returns sum of a list"""
        result: float = sum(self.values)
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Defines what it means to add in Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                new_value: float = self.values[i] + rhs.values[i]
                result.values.append(new_value)
            return result
        if isinstance(rhs, float):
            for value in self.values:
                value += rhs
                result.values.append(value)
            return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Defines what it means to power operate in Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                new_value: float = self.values[i] ** rhs.values[i]
                result.values.append(new_value)
                i += 1
            return result
        if isinstance(rhs, float):
            for value in self.values:
                value ** rhs
                result.values.append(value)
            return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                truth: bool = (self.values[i] == rhs.values[i])
                result.append(truth)
                i += 1
            return result
        if isinstance(rhs, float):
            for value in self.values:
                truth: bool = (rhs == value)
                result.append(truth)
            return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                truth: bool = (self.values[i] > rhs.values[i])
                result.append(truth)
                i += 1
            return result
        if isinstance(rhs, float):
            for value in self.values:
                truth: bool = (rhs > value)
                result.append(truth)
            return result

    def __getitem__(self, rhs: int) -> float:
        """Gives Simply subscription operator abilities."""
        result: float = self.values[rhs]
        return result

    # TODO: Your constructor and methods will go here.