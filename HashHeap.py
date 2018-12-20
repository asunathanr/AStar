import heapq


"""
File: HashHeap.py
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

    def add(self, node):
        """
        Adds key to heap and key value pair to hash table.
        Only adds if it is beneficial to do so. (Is lowest value associated with that key)
        :param node:
        """
        self.table[node.value] = node
        heapq.heappush(self.heap, node)

    def should_replace_node(self, new_weight, new_value) -> bool:
        """
        :param new_weight:
        :param new_value:
        :return: If it is cheaper to travel new path opposed to path already stored in system.
        """
        if self.find(new_value) is None:
            return True
        else:
            if new_weight < self.table[new_value].weight:
                return True
            else:
                return False

    def top(self):
        """
        :return: The top item on the heap or None if nothing is on the heap.
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
        return node

    def find(self, node_value):
        if node_value in self.table:
            return self.table[node_value]
        return None

    def __len__(self):
        return len(self.heap)
