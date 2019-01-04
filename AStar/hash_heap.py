import heapq
from AStar.search_node import SearchNode


"""
File: hash_heap.py
Author: Nathan Robertson
Purpose:
    Create a HashHeap interface specifically for the AStar class to use as its open set.
    Abstracts heap functions, auxiliary hashing, and checking table for updates
"""


class HashHeap:
    """
    A structure which allows both fast search and fast heaping.
    The heap structure controls addition/removal of items
    Found this idea at: https://github.com/jonasnick/A-star/blob/master/astar/datastructures/HashPriorityQueue.java
    """
    def __init__(self):
        self.heap = []
        self.table = {}
        self.current = None

    @staticmethod
    def initialize(start):
        new_heap = HashHeap()
        new_heap.add(SearchNode(0, start))
        return new_heap

    def add(self, node) -> None:
        """
        Procedure which adds key to heap and key value pair to hash table.
        :param node:
        """
        self.table[node.value] = node
        heapq.heappush(self.heap, node)

    def is_cheaper(self, new_weight, new_value) -> bool:
        """
        :param new_weight:
        :param new_value:
        :return: If it is cheaper to travel new path opposed to path already stored in system.
        """
        if not self.has(new_value) or new_weight < self.table[new_value].weight:
            return True
        return False

    def top(self):
        """
        :return: The smallest item in the heap or None if nothing is in the heap.
        """
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def pop(self):
        """
        Removes cheapest node from heap and table.
        :return: Cheapest node in heap
        """
        node = heapq.heappop(self.heap)
        if self.find(node.value) is not None:
            self.table.pop(node.value)
        self.current = node
        return node

    def has(self, value) -> bool:
        return value in self.table

    def find(self, node_value):
        if node_value in self.table:
            return self.table[node_value]
        else:
            return None

    def __len__(self):
        return len(self.heap)
