from Coordinate.coord import Coord
from hash_heap import *
from search_node import SearchNode

"""
File: a_star.py
Author: Nathan Robertson
Purpose:
    Implement a fast fairly generic AStar algorithm.
    See: http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
"""


class AStar:
    def __init__(self, graph, heuristic_fn):
        """
        :param graph: A graph object which needs these methods: \n
                      1. neighbors(node): Should return all valid neighbors of a node. \n
                      2. Cost(): Returns the cost to travel from a neighbor of node to node. \n
        :param heuristic_fn: The heuristic used to direct A* towards the goal node. \n
                             It should be able to take two arguments: A neighbor and the goal.
        """
        self.graph = graph
        self.heuristic_fn = heuristic_fn

    def execute(self, endpoints: (Coord, Coord)):
        """
        Attempt to find quickest path from start to end.
        :param endpoints: Start node and goal node values.
        :return: A list of nodes from start to end if successful, an empty list if not.
        """
        start, goal = endpoints
        if start == goal:
            return [start]
        elif not self.graph.neighbors(goal):
            return []
        open_set = HashHeap()
        open_set.add(SearchNode(0, start))
        closed_set = set()
        cost = self.graph.cost()
        while not self.is_goal_reached(open_set.top(), goal):
            current = open_set.pop()
            closed_set.add(current.value)
            neighbors = [neighbor for neighbor in self.graph.neighbors(current.value) if neighbor not in closed_set]
            weight = current.weight
            new_g = cost + weight
            for neighbor in neighbors:
                if open_set.has(neighbor):
                    h = new_g + self.heuristic_fn(neighbor, goal)
                    if open_set.should_replace_node(h, neighbor):
                        node = open_set.find(neighbor)
                        node.parent = current
                        node.weight = new_g
                        node.f = new_g + h
                        open_set.add(node)
                else:
                    new_node = SearchNode(weight + cost, neighbor, current, new_g + self.heuristic_fn(neighbor, goal))
                    open_set.add(new_node)
        return self.extract_value(self.find_path(open_set.top()))

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
        :param goal: The last node in the path. Needs to have its parent saved in the parent field.
        """
        if goal is None:
            return []
        return self.find_path(goal.parent) + [goal]


class ClosedSet:
    """
    Closed set used in A* implementation.
    """
    def __init__(self):
        self.closed = set()

    def add(self, item, weight) -> None:
        self.closed.add(item)

    def find(self, item) -> bool:
        return item in self.closed
