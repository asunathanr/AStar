from coord import Coord
import enum


"""
File: direction.py
Author: Nathan Robertson
Purpose:
    Encapsulates the directions a unit is allowed to move on a grid. Can be thought of as also encapsulating next cell
    to move to.
"""


class Directions(enum.Enum):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3
    TOP_LEFT = 4
    TOP_RIGHT = 5
    BOTTOM_LEFT = 6
    BOTTOM_RIGHT = 7


class Direction:

    def __init__(self):
        self.straight_coordinates = {
            Directions.TOP: Coord(-1, 0),
            Directions.BOTTOM: Coord(1, 0),
            Directions.LEFT: Coord(0, -1),
            Directions.RIGHT: Coord(0, 1),
        }
        self.diagonal_coordinates = {
            Directions.TOP_LEFT: Coord(-1, -1),
            Directions.TOP_RIGHT: Coord(1, 1),
            Directions.BOTTOM_LEFT: Coord(-1, 1),
            Directions.BOTTOM_RIGHT: Coord(-1, 1)
        }

    def top(self) -> Coord:
        return self.straight_coordinates[Directions.TOP]

    def bottom(self) -> Coord:
        return self.straight_coordinates[Directions.BOTTOM]

    def left(self) -> Coord:
        return self.straight_coordinates[Directions.LEFT]

    def right(self) -> Coord:
        return self.straight_coordinates[Directions.RIGHT]

    def top_left(self):
        return self.diagonal_coordinates[Directions.TOP_LEFT]

    def top_right(self):
        return self.diagonal_coordinates[Directions.TOP_RIGHT]

    def bottom_left(self):
        return self.diagonal_coordinates[Directions.BOTTOM_LEFT]

    def bottom_right(self):
        return self.diagonal_coordinates[Directions.BOTTOM_RIGHT]

    def all_directions(self) -> {}:
        return {self.top(), self.bottom(), self.left(), self.right(), self.top_left(), self.top_right(), self.bottom_left(), self.bottom_right()}


global_direction = Direction()
