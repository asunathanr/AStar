from weighted_coord import Coord, WeightedCoord
from HashHeap import HashHeap


# File: AStar.py
# Authors: Eric Day, Hey Joe, Nathan Robertson
# Purpose: Implement the A* algorithm using the MapGrid class
# A* is a path finding algorithm used to find the best approximate path between two nodes in a graph.


class PathMaker:
    """
    Creates paths on a grid.
    """

    def __init__(self, grid):
        self.grid = grid
        self.PATH_OUT_OF_BOUNDS = None
        self.SAME_CELL = []
        self.INVALID_PATH = []

    def make(self, algorithm) -> []:
        if algorithm.start == algorithm.end:
            return self.SAME_CELL
        if not self.is_valid_coord(algorithm.start) or not self.is_valid_coord(algorithm.end):
            return self.PATH_OUT_OF_BOUNDS
        last_cell = algorithm.execute()
        path = self.make_path(last_cell)
        return self.remove_weights(path)

    def is_valid_coord(self, coord: Coord):
        return self.grid.is_valid_coord(coord)

    def remove_weights(self, path: []) -> []:
        return list(map(lambda cell: cell.value, path))

    def make_path(self, end):
        return self.find_path(end)

    def find_path(self, weighted_end):
        if weighted_end is None:
            return []
        return self.find_path(weighted_end.parent) + [weighted_end]



