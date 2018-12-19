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
        :return:
        """
        if self.find(node) is None:
            self.table[node] = node.f
            heapq.heappush(self.heap, node)
        else:
            if node.f < self.table[node]:
                self.table[node.f] = node
                heapq.heappush(self.heap, node)

    def should_update(self, node) -> bool:
        stored_node = self.find(node)
        if stored_node is None:
            return True
        elif node.weight < stored_node.weight:
            return True
        else:
            return False

    def top(self):
        """
        :return: The top item on the heap
        """
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def pop(self):
        value = heapq.heappop(self.heap)
        if self.find(value) is not None:
            self.table.pop(value)
        return value

    def find(self, node):
        if node in self.table:
            return self.table[node]
        return None

    def __len__(self):
        return len(self.heap)
