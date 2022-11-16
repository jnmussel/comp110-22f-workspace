"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730471672"


class Simpy:
    """Defines class Simpy."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Constructor."""
        self.values = values

    def __repr__(self) -> str:
        """Repr for printing."""
        return f"Simpy({self.values})"

    def fill(self, the_float: float, the_int: int) -> None:
        """Fills a list with a specific number of repeating values."""
        self.values = []
        for _ in range(the_int):
            self.values.append(the_float)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in a list with a start, stop, and step."""
        while abs(start) < abs(stop):
            self.values.append(start)
            start += step
        
    def sum(self) -> float:
        """Returns sum of a list."""
        result: float = sum(self.values)
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Defines what it means to add in Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
            return result
        else:
            for value in range(len(self.values)):
                new_value: float = self.values[value] + rhs
                result.values.append(new_value)
            return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Defines what it means to power operate in Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
            return result
        else:
            for value in range(len(self.values)):
                new_value: float = self.values[value] ** rhs
                result.values.append(new_value)
            return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Defines equal."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
            return result
        if isinstance(rhs, float):
            for value in self.values:
                truth: bool = (rhs == value)
                result.append(truth)
            return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than function."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for value in range(len(self.values)):
                if self.values[value] > rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Gives Simply subscription operator abilities."""
        if isinstance(rhs, int):
            result: float = self.values[rhs]
            return result
        else:
            result: Simpy = Simpy([])
            for _ in range(len(rhs)):
                if rhs[_] is True:
                    result.values.append(self.values[_])
            return result