from diagonal_grid import DiagonalGrid
import heapq
from jps_node import JPSNode
from coord import Coord

"""
File: jump_point_search.py
Author: Nathan Robertson
Purpose:
    Implements jump point search found here: http://grastien.net/ban/articles/hg-aaai11.pdf
"""


NEXT_DIAGONALS = frozenset({(1, 1), (-1, -1), (-1, 1), (1, -1)})


class OpenSet:
    def __init__(self):
        self.heap = []
        self.values = set()

    def add(self, jump_node):
        if jump_node not in self.values:
            heapq.heappush(self.heap, jump_node)
            self.values.add(jump_node)

    def top(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def pop(self):
        if len(self.heap) > 0:
            value = heapq.heappop(self.heap)
            self.values.remove(value)
            return value
        return None

    def find(self, value):
        return value in self.values

    def __len__(self):
        return len(self.heap)


class JumpPointSearch:
    def __init__(self, grid, heuristic_fn):
        self.grid = grid
        self.heuristic_fn = heuristic_fn

    def execute(self, endpoints: (Coord, Coord)):
        start, goal = endpoints
        start_node = JPSNode(start, None, 0, self.heuristic_fn(start, goal))
        open_set = OpenSet()
        jump_points = [start_node]
        for successor in self.successors(start_node, start, goal):
            open_set.add(successor)
        while len(open_set) > 0 and open_set.top().coord != goal:
            current = open_set.pop()
            jump_points.append(current)
            for successor in self.successors(current, start, goal):
                open_set.add(successor)
        goal_node = next((x for x in open_set.heap if x.coord == goal), None)
        jump_points.append(goal_node)
        return jump_points

    def successors(self, current: JPSNode, start, goal: Coord):
        succ = set()
        neighbors = self.prune(current)
        parent_x, parent_y = current.coord.x, current.coord.y
        for neighbor in neighbors:
            dir_coord = self.direction(current.coord, neighbor)
            next_jump_point = self.jump((parent_x, parent_y), (dir_coord.x, dir_coord.y), start, goal)
            if next_jump_point is not None:
                next_node = JPSNode(next_jump_point, dir_coord)
                next_node.g = current.g + 1
                next_node.f = next_node.g + self.heuristic_fn(next_node.coord, goal)
                succ.add(next_node)
        return succ

    def connect_path(self, jump_points: []):
        def connect_jump_points(begin, end):
            total_cells = int(self.heuristic_fn(begin.coord, end.coord))
            return list(map(lambda offset: Coord(begin.coord.x + end.direction.x * offset, begin.coord.y + end.direction.y * offset), range(0, total_cells)))

        path = []
        for i in range(0, len(jump_points) - 1):
            begin = jump_points[i]
            end = jump_points[i + 1]
            path += connect_jump_points(begin, end)
        path.append(jump_points[len(jump_points) - 1].coord)
        return path

    def jump(self, initial_node: (int, int), direction: (int, int), start, goal):
        next_x, next_y = initial_node[0] + direction[0], initial_node[1] + direction[1]
        next_coord = Coord(next_x, next_y)
        if not self.grid.is_valid_coord(next_coord):
            return None
        elif next_coord in self.grid.obstacles():
            return None
        elif next_coord == goal:
            return next_coord
        forced_neighbors = set(filter(lambda node: node in self.grid.obstacles(), self.grid.neighbors(next_coord)))
        if len(forced_neighbors) > 0:
            return next_coord
        if direction in NEXT_DIAGONALS:
            for i in {(0, direction[1]), (direction[0], 0)}:
                if self.jump((next_x, next_y), i, start, goal) is not None:
                    return next_coord
        return self.jump((next_x, next_y), direction, start, goal)

    def prune(self, current: JPSNode):
        if current.direction is None:
            return self.grid.neighbors(current.coord)
        direction = current.direction.x, current.direction.y
        if direction in NEXT_DIAGONALS:
            coord = current.coord
            possible_neighbors = [Coord(current.coord.x, current.coord.y + current.direction.y), Coord(coord.x + current.direction.x, coord.y), Coord(coord.x + current.direction.x, coord.y + current.direction.y)]
            return list(filter(lambda neighbor: self.grid.is_adjacent(coord, neighbor), possible_neighbors))
        else:
            next_pos = Coord(current.coord.x + current.direction.x, current.coord.y + current.direction.y)
            if self.grid.is_adjacent(current.coord, next_pos):
                return [next_pos]
            return []

    def direction(self, parent: Coord, current: Coord):
        return Coord(current.x - parent.x, current.y - parent.y)
