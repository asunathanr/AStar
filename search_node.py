"""
File: search_node.py
Author: Nathan Robertson
Purpose: Create a search node class to be used by A*
"""


class SearchNode:
    __slots__ = ('weight', 'value', 'value', 'parent', 'f')

    def __init__(self, weight, value, parent=None, f=0):
        self.weight = weight
        self.value = value
        self.parent = parent
        self.f = f

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