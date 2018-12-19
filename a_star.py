from coord import Coord
from HashHeap import *

"""
File: a_star.py
Author: Nathan Robertson
Purpose:
    Implement a fast fairly generic AStar algorithm.
"""


class ClosedSet:
    """
    Closed set used in A* implementation.
    """
    def __init__(self):
        self.closed = {}

    def add(self, item, weight) -> None:
        self.closed[item] = weight

    def find(self, item) -> bool:
        return item in self.closed


class SearchNode:
    __slots__ = ('weight', 'value', 'value', 'parent', 'h', 'f')

    def __init__(self, weight, value, parent=None):
        self.weight = weight
        self.value = value
        self.parent = parent
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        """
        :param other: Either another SearchNode or a node of the same type returned by a search node's value attribute
        :return: Whether one SearchNode's value is equivalent to another.
        """
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return self.value == other

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash(self.value)


class AStar:
    """
    Creates a path from start to goal using a heuristic function and a grid structure.
    """

    def __init__(self, grid, endpoints: (Coord, Coord), heuristic_fn):
        self.grid = grid
        self.heuristic_fn = heuristic_fn
        self.start, self.end = endpoints
        self.open_set = HashHeap()
        self.weighted_start = SearchNode(0, self.start)
        self.open_set.add(self.weighted_start)
        self.closed_set = ClosedSet()

    def execute(self) -> (SearchNode, bool):
        """
        Attempt to find quickest path from start to end.
        This starts the "procedural" part of the algorithm. It seems best to treat this part procedurally so far.
        :return: Next to last node of path and if an actual path was found from start to end
        """
        if self.start == self.end:
            return [self.start]
        while not self.is_goal_reached(self.open_set.top(), self.end):
            current = self.open_set.pop()
            self.closed_set.add(current.value, current.weight)
            neighbors = self.grid.neighbors(current.value)
            for neighbor in neighbors:
                if not self.closed_set.find(neighbor):
                    new_g = current.weight + self.grid.cost(neighbor)
                    if self.open_set.should_replace_node(new_g, neighbor):
                        new_node = SearchNode(new_g, neighbor, current)
                        new_node.h = self.heuristic_fn(neighbor, self.end)
                        new_node.f = new_g + new_node.h
                        self.open_set.add(new_node)
        return self.remove_weights(self.find_path(self.open_set.top()))

    def is_goal_reached(self, current, goal):
        return current is None or current == goal

    def remove_weights(self, path: []) -> []:
        return list(map(lambda cell: cell.value, path))

    def make_path(self, end):
        return self.find_path(end)

    def find_path(self, weighted_end):
        if weighted_end is None:
            return []
        return self.find_path(weighted_end.parent) + [weighted_end]
