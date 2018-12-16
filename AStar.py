from MapGrid import MapGrid
from weighted_coord import Coord, WeightedCoord
from HashHeap import HashHeap

# File: AStar.py
# Authors: Eric Day, Hey Joe, Nathan Robertson
# Purpose: Implement the A* algorithm using the MapGrid class
# A* is a path finding algorithm used to find the best approximate path between two nodes in a graph.


class AStar(MapGrid):
    def __init__(self, xsize, ysize, obstacles: list):
        super().__init__(xsize, ysize, obstacles)
        self.PATH_OUT_OF_BOUNDS = None
        self.INVALID_PATH = []

    def a_star(self, start: Coord, end: Coord) -> []:
        if start == end:
            return []
        if not self.is_valid_coord(start) or not self.is_valid_coord(end):
            return self.PATH_OUT_OF_BOUNDS
        last_cell, successful = self.PathMaker(self, start, end).make()
        path = self.make_path(last_cell, end) if successful else self.INVALID_PATH
        return path

    def manhattan(self, coord1, coord2):
        return abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)

    def make_path(self, parent, end):
        weighted_end = WeightedCoord(0, end.x, end.y)
        weighted_end.parent = parent
        return self.find_path(weighted_end)

    def find_path(self, weighted_end):
        if weighted_end is None:
            return []
        return self.find_path(weighted_end.parent) + [weighted_end]

    class PathMaker:
        """
        Creates paths from start to one goal using manhattan distance heuristics and a grid structure.
        This is the meat of the A* implementation.
        """
        def __init__(self, astar, start: Coord, end: Coord):
            self.astar = astar
            self.start = start
            self.end = end
            self.open_set = HashHeap()
            self.open_set.add(0, WeightedCoord(0, start.x, start.y))
            self.closed_set = set()
            self.current = self.open_set.top()
            self.neighbors = self.next_neighbors()

        def make(self) -> (WeightedCoord, bool):
            while len(self.open_set) > 0 and self.end not in self.neighbors:
                self.process_cell()
            return self.current, self.end in self.neighbors

        def process_cell(self):
            self.open_set.pop()
            cheaper_neighbors = self.neighbors_to_update()
            new_cells = map(lambda neighbor: self.make_new_cell(neighbor), cheaper_neighbors)
            self.add_new_cells(new_cells)
            self.closed_set.add(self.current)
            self.current = self.open_set.top()
            self.neighbors = self.next_neighbors()

        def add_new_cells(self, new_cells):
            for cell in new_cells:
                self.add_cell(cell)

        def next_neighbors(self) -> []:
            neighbors = list(filter(lambda n: n not in self.closed_set, self.astar.neighbors(self.current)))
            return neighbors

        def neighbors_to_update(self):
            calc_g = lambda n: self.current.weight + self.astar.cost(n)
            return filter(lambda x: self.should_replace_cell(calc_g(x)), self.neighbors)

        def should_replace_cell(self, new_g):
            old_value = self.open_set.find(self.current)
            if old_value is None:
                return True
            if self.current == old_value and new_g < old_value.weight:
                return True
            return False

        def add_cell(self, new_cell):
            self.open_set.add(new_cell.weight, new_cell)

        def make_new_cell(self, location) -> WeightedCoord:
            new_cell = WeightedCoord(self.current.weight + self.astar.cost(location), location.x, location.y, self.current)
            new_cell.h = self.astar.manhattan(new_cell, self.end)
            return new_cell
