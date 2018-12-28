"""
File: jps_node.py
Author: Nathan Robertson
Purpose:
    Represents a node for the Jump Point Search algorithm.
"""


class JPSNode:
    def __init__(self, coord, direction, g=0, f=0):
        self.coord = coord
        self.direction = direction
        self.f = g
        self.g = f

    def __le__(self, other):
        return self.f < other.f
