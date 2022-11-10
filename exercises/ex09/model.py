"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi


__author__ = "730471672"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other_point: Point) -> float:
        """Returns distance between two points."""
        result: float = 0.0
        from math import sqrt
        result = sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return result


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Tick function."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            tick += 1
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Infects a cell."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Makes a cell vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Defines a cell as infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_immune():
            return "yellow"
        if self.is_infected():
            return "purple"

    def contact_with(self, other_cell: Cell) -> None:
        """When two cells make contact."""
        if self.is_immune():
            self.immunize()
        elif other_cell.is_vulnerable() and self.is_infected():
            self.contract_disease()
            other_cell.contract_disease()

    def immunize(self) -> None:
        """Assigns IMMUNE constant to sickness attribute of the cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Checks if sickness attribute is equal to IMMUNE constant."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int):
        """Initialize the cells with random locations and directions."""
        immunecells: int = 0
        if infected_cells <= 0:
            raise ValueError("Infected cells can't exceed regular cells or be less than zero.")
        elif infected_cells >= cells:
            raise ValueError("Infected cells can't exceed regular cells or be less than zero.")
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(infected_cells):
            self.population[_].contract_disease()
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_X:
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_X:
            cell.direction.y *= -1.0

    def check_contacts(self, other_cell: Cell) -> None:
        """Checks of two cells run into each other.""",
        i: int = 0
        j: int = i + 1
        while i < len(self.population):
            j = i + 1
            while j < len(self.population):
                dist: float = self.population[i].location.distance(self.population[j].location)
                if dist < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i: int = 0
        for cell in self.population:
            if cell.is_vulnerable() or cell.is_immune():
                i += 1
        if i == len(self.population):
            return True
        return False