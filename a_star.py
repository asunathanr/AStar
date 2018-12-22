from coord import Coord
from HashHeap import *
from search_node import SearchNode

"""
File: a_star.py
Author: Nathan Robertson
Purpose:
    Implement a fast fairly generic AStar algorithm.
    See: http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
"""


class AStar:
    def __init__(self, graph, endpoints: (Coord, Coord), heuristic_fn):
        self.graph = graph
        self.heuristic_fn = heuristic_fn
        self.start, self.goal = endpoints
        self.open_set = HashHeap()
        self.open_set.add(SearchNode(0, self.start))
        self.closed_set = ClosedSet()

    def execute(self) -> (SearchNode, bool):
        """
        Attempt to find quickest path from start to end.
        :return: A list of nodes from start to end if successful, an empty list if not.
        """
        if self.start == self.goal:
            return [self.start]
        while not self.is_goal_reached(self.open_set.top(), self.goal):
            current = self.open_set.pop()
            self.closed_set.add(current.value, current.weight)
            neighbors = self.graph.neighbors(current.value)
            for neighbor in neighbors:
                if not self.closed_set.find(neighbor):
                    new_g = current.weight + self.graph.cost(neighbor)
                    if self.open_set.should_replace_node(new_g, neighbor):
                        new_node = SearchNode(new_g, neighbor, current)
                        new_node.h = self.heuristic_fn(neighbor, self.goal)
                        new_node.f = new_g + new_node.h
                        self.open_set.add(new_node)
        return self.extract_value(self.find_path(self.open_set.top()))

    def is_goal_reached(self, current, goal):
        """
        :param current: The cheapest node at this moment in time.
        :param goal: Final node of path.
        :return: If current node is goal node or if there are no new nodes to process then there is no viable path from
        start to end.
        """
        return current is None or current == goal

    def extract_value(self, path: []) -> []:
        """
        Goes through each search node, pulls out the value, and returns the new list.
        :param path: A list of nodes on a grid that form a path.
        :return: List of node values (e.g. if working with grid would be coordinates)
        """
        return list(map(lambda cell: cell.value, path))

    def find_path(self, goal: SearchNode):
        """
        Traverse end's parents until at start and capture that into a list
        :param goal:
        """
        if goal is None:
            return []
        return self.find_path(goal.parent) + [goal]


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
