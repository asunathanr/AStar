from MapGrid import MapGrid
from weighted_coord import Coord, WeightedCoord

# File: AStar.py
# Authors: Eric Day, Joe, Nathan Robertson
# Purpose: Implement the AStar algorithm using the MapGrid class


class AStar(MapGrid):
    def __init__(self, xsize, ysize, obstacles: list):
        super().__init__(xsize, ysize, obstacles)
        self.PATH_OUT_OF_BOUNDS = None
        self.INVALID_PATH = []

    def a_star(self, start: Coord, end: Coord) -> []:
        if not self.is_valid_coord(start) or not self.is_valid_coord(end):
            return self.PATH_OUT_OF_BOUNDS
        last_cell, successful = self.create_path(start, end)
        path = self.make_path(last_cell, end) if successful else self.INVALID_PATH
        return path

    def create_path(self, start, end) -> (WeightedCoord, bool):
        open_set, closed_set = self.initialize(start)
        current, neighbors = self.next_cell(open_set, closed_set)
        while len(open_set) > 0 and end not in neighbors:
            open_set.remove(current)
            cheaper_neighbors = self.neighbors_to_update(current, neighbors, open_set)
            new_cells = map(lambda neighbor: self.make_new_cell(current.weight + self.cost(neighbor), neighbor, current, end), cheaper_neighbors)
            for cell in new_cells:
                open_set = self.add_cell(cell, open_set)
            closed_set.add(current)
            current, neighbors = self.next_cell(open_set, closed_set)
        return current, end in neighbors

    def neighbors_to_update(self, current, neighbors, open_set):
        calc_g = lambda n: current.weight + self.cost(n)
        return filter(lambda x: self.should_replace_cell(calc_g(x), current, open_set), neighbors)

    def initialize(self, start: Coord):
        """
        Create initial data structures to traverse grid with.
        """
        return {WeightedCoord(0, start.x, start.y)}, set()

    def next_cell(self, open_set, closed_set) -> ():
        current = self.pick_current(open_set)
        neighbors = list(filter(lambda n: n not in closed_set, self.neighbors(current)))
        return current, neighbors

    def pick_current(self, open_set):
        if len(open_set) > 0:
            current = min(open_set)
        else:
            current = None
        return current

    def manhattan(self, coord1, coord2):
        return abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)

    def add_cell(self, new_cell, open_set):
        if new_cell in open_set:
            open_set.remove(new_cell)
        open_set.add(new_cell)
        return open_set

    def try_add_cell(self, cell, open_set, parent, end):
        new_g = parent.weight + self.cost(cell)
        if self.should_replace_cell(new_g, cell, open_set):
            new_cell = self.make_new_cell(new_g, cell, parent, end)
            if new_cell in open_set:
                open_set.remove(new_cell)
            open_set.add(new_cell)
        return open_set

    def should_replace_cell(self, new_g, cell, open_set):
        if cell not in open_set:
            return True
        for i in open_set:
            if cell == i and new_g < i.weight:
                return True
        return False

    def make_new_cell(self, weight, location, parent, end) -> WeightedCoord:
        new_cell = WeightedCoord(weight, location.x, location.y, parent)
        new_cell.h = self.manhattan(new_cell, end)
        return new_cell

    def make_path(self, parent, end):
        weighted_end = WeightedCoord(0, end.x, end.y)
        weighted_end.parent = parent
        return self.find_path(weighted_end)

    def find_path(self, weighted_end):
        if weighted_end is None:
            return []
        return self.find_path(weighted_end.parent) + [weighted_end]
