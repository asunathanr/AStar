from Coordinate.coord import Coord
from AStar.hash_heap import *
from AStar.search_node import SearchNode

"""
File: a_star.py
Author: Nathan Robertson
Purpose:
    Implement a fast fairly generic AStar algorithm.
    See: http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
"""


PATH_OUT_OF_BOUNDS = []


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

    def execute(self, endpoints):
        """
        Attempt to find quickest path from start to end.
        :param endpoints: Start node and goal node values.
        :return: A list of nodes from start to end if successful, an empty list if not.
        """
        start, goal = endpoints
        if start == goal:
            path = [start]
        elif not self.graph.neighbors(goal) or not self.graph.neighbors(goal):
            path = PATH_OUT_OF_BOUNDS
        else:
            path = self._raw_execute(start, goal)
        return path

    def _raw_execute(self, start, goal):
        open_set = HashHeap.initialize(start)
        closed_set = set()
        while not self.is_goal_reached(open_set.top(), goal):
            current = open_set.pop()
            closed_set.add(current.value)
            new_g = self.graph.cost() + current.weight
            for neighbor in [neighbor for neighbor in self.graph.neighbors(current.value) if
                             neighbor not in closed_set]:
                if open_set.is_cheaper(new_g, neighbor):
                    new_node = SearchNode(new_g, neighbor, current, new_g + self.heuristic_fn(neighbor, goal))
                    open_set.add(new_node)
        return self.extract_value(self.find_path(open_set.top()))

    def is_goal_reached(self, current, goal):
        """
        :param current: The cheapest node at this moment in time.
        :param goal: Final node of path.
        :return: If current node is goal node or if there are no new nodes to process.
        """
        return current is None or current == goal

    def extract_value(self, path: []) -> []:
        """
        Goes through each search node, pulls out the value, and returns the new list.
        This method is for returning the pure path to the client instead of all the details that went into the search.
        :param path: A list of nodes on a grid that form a path.
        :return: List of node values (e.g. if working with grid would be coordinates)
        """
        return list(map(lambda cell: cell.value, path))

    def find_path(self, goal: SearchNode) -> []:
        """
        Translate parent pointers into a path.
        :param goal: The last node in the path. Needs to have its parent saved in the parent field.
        """
        current = goal
        path = []
        while current is not None:
            path.append(current)
            current = current.parent
        return path
