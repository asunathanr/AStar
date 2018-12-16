from MapGrid import MapGrid
from weighted_coord import Coord, WeightedCoord

# File: AStar.py
# Authors: Eric Day, Hey Joe, Nathan Robertson
# Purpose: Implement the AStar algorithm using the MapGrid class


class AStar(MapGrid):
    def __init__(self, xsize, ysize, obstacles: list):
        super().__init__(xsize, ysize, obstacles)
        self.PATH_OUT_OF_BOUNDS = None
        self.INVALID_PATH = []

    def a_star(self, start: Coord, end: Coord) -> []:
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
        def __init__(self, astar, start: Coord, end: Coord):
            self.astar = astar
            self.start = start
            self.end = end
            self.open_set, self.closed_set = self.initialize(start)
            self.current, self.neighbors = self.next_cell()

        def make(self) -> (WeightedCoord, bool):
            while len(self.open_set) > 0 and self.end not in self.neighbors:
                self.process_cell()
            return self.current, self.end in self.neighbors

        def process_cell(self):
            self.open_set.remove(self.current)
            cheaper_neighbors = self.neighbors_to_update()
            new_cells = map(lambda neighbor: self.make_new_cell(neighbor), cheaper_neighbors)
            self.add_new_cells(new_cells)
            self.closed_set.add(self.current)
            self.current, self.neighbors = self.next_cell()

        def add_new_cells(self, new_cells):
            for cell in new_cells:
                self.open_set = self.add_cell(cell)

        def initialize(self, start: Coord):
            """
            Create initial data structures to traverse grid with.
            """
            return {WeightedCoord(0, start.x, start.y)}, set()

        def pick_current(self, open_set):
            if len(open_set) > 0:
                current = min(open_set)
            else:
                current = None
            return current

        def next_cell(self) -> ():
            current = self.pick_current(self.open_set)
            neighbors = list(filter(lambda n: n not in self.closed_set, self.astar.neighbors(current)))
            return current, neighbors

        def neighbors_to_update(self):
            calc_g = lambda n: self.current.weight + self.astar.cost(n)
            return filter(lambda x: self.should_replace_cell(calc_g(x)), self.neighbors)

        def should_replace_cell(self, new_g):
            if self.current not in self.open_set:
                return True
            for i in self.open_set:
                if self.current == i and new_g < i.weight:
                    return True
            return False

        def add_cell(self, new_cell):
            if new_cell in self.open_set:
                self.open_set.remove(new_cell)
            self.open_set.add(new_cell)
            return self.open_set

        def make_new_cell(self, location) -> WeightedCoord:
            new_cell = WeightedCoord(self.current.weight + self.astar.cost(location), location.x, location.y, self.current)
            new_cell.h = self.astar.manhattan(new_cell, self.end)
            return new_cell
