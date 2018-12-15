from MapGrid import *


class AStar(MapGrid):
    def __init__(self, xsize, ysize, obstacles: list):
        super().__init__(xsize, ysize, obstacles)

    def a_star(self, start: Coord, end: Coord):
        if not self.is_valid_coord(start) or not self.is_valid_coord(end):
            return None
        processing, visited = self.initialize(start)
        current, neighbors = self.next_cell(processing, visited)
        while len(processing) > 0 and end not in neighbors:
            processing.remove(current)
            for neighbor in neighbors:
                tentative_g = current.weight + self.gridArea[neighbor.x][neighbor.y]
                if self.should_replace_cell(tentative_g, current, processing):
                    new_cell = self.make_new_cell(tentative_g, neighbor, end)
                    if new_cell in processing:
                        processing.remove(new_cell)
                    processing.add(new_cell)
            visited.add(current)
            current, neighbors = self.next_cell(processing, visited)
        return visited

    def initialize(self, start):
        return {WeightedCoord(0, start.x, start.y)}, set()

    def next_cell(self, open_set, closed_set) -> ():
        current = self.pick_current(open_set)
        neighbors = filter(lambda n: n not in closed_set, self.neighbors(current))
        return current, neighbors

    def pick_current(self, open_set):
        if len(open_set) > 0:
            current = min(open_set)
        else:
            current = None
        return current

    def manhattan(self, coord1, coord2):
        return abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)

    def try_add_cell(self, new_g, cell, open_set, end):
        if self.should_replace_cell(new_g, cell, open_set):
            new_cell = self.make_new_cell(new_g, cell, end)
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

    def make_new_cell(self, weight, location, end) -> WeightedCoord:
        new_cell = WeightedCoord(weight, location.x, location.y)
        new_cell.h = self.manhattan(new_cell, end)
        return new_cell
