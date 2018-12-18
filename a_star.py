from weighted_coord import WeightedCoord
from coord import Coord
from HashHeap import HashHeap


class AStar:
    """
    Creates a path from start to goal using a heuristic function and a grid structure.
    """

    def __init__(self, grid, endpoints: (Coord, Coord), heuristic_fn):
        self.grid = grid
        self.heuristic_fn = heuristic_fn
        self.start, self.end = endpoints
        self.open_set = HashHeap()
        self.open_set.add(0, WeightedCoord(0, self.start.x, self.start.y))
        self.closed_set = {}
        self.setup_closed_set()
        self.current = self.open_set.top()
        self.neighbors = self.next_neighbors()

    def execute(self) -> (WeightedCoord, bool):
        """
        Attempt to find quickest path from start to end.
        This starts the "procedural" part of the algorithm. It seems best to treat this part procedurally so far.
        :return: Next to last node of path and if an actual path was found from start to end
        """
        while len(self.open_set) > 0 and self.end not in self.neighbors:
            self.open_set.pop()
            self.process_cell()
            self.current = self.open_set.top()
            self.neighbors = self.next_neighbors()
        return self.current, self.end in self.neighbors

    def process_cell(self):
        """
        Given the current cell and neighbors not in closed set for that cell update open set with new information.
        Add it to closed set once finished
        """
        cheaper_neighbors = self.neighbors_to_update()
        new_cells = map(lambda neighbor: self.make_new_cell(neighbor), cheaper_neighbors)
        self.add_new_cells(new_cells)
        self.closed_set[Coord(self.current.x, self.current.y)] = True

    def add_new_cells(self, new_cells) -> None:
        """
        Add cells that are potentially part of the cheapest path.
        :param new_cells:
        """
        for cell in new_cells:
            self.open_set.add(cell.weight, cell)

    def next_neighbors(self) -> []:
        neighbors = list(filter(lambda n: not self.closed_set[n], self.grid.neighbors(self.current)))
        return neighbors

    def neighbors_to_update(self):
        calc_g = lambda n: self.current.weight + self.grid.cost(n)
        return filter(lambda x: self.should_replace_cell(calc_g(x)), self.neighbors)

    def should_replace_cell(self, new_g):
        old_value = self.open_set.find(self.current)
        if old_value is None:
            return True
        if self.current == old_value and new_g < old_value.weight:
            return True
        return False

    def make_new_cell(self, location) -> WeightedCoord:
        new_cell = WeightedCoord(self.current.weight + self.grid.cost(location), location.x, location.y, self.current)
        dx1 = location.x - self.end.x
        dy1 = location.y - self.end.y
        dx2 = self.start.x - self.end.x
        dy2 = self.start.y - self.start.x
        cross = abs(dx1 * dy2 - dx2 * dy1)
        new_cell.h = self.heuristic_fn(location, self.end) + cross * 0.001
        new_cell.set_f()
        return new_cell

    def setup_closed_set(self):
        for i in range(0, self.grid.xsize):
            for j in range(0, self.grid.ysize):
                self.closed_set[Coord(i, j)] = False