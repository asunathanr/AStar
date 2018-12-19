import heapq

"""
File: HashHeap.py
Author: Nathan Robertson
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

    def add(self, key, value):
        """
        Adds key to heap and key value pair to hash table.
        Only adds if it is beneficial to do so. (Is lowest value associated with that key)
        :param key:
        :param value:
        :return:
        """
        if self.find(key) is None:
            self.table[key] = value
            heapq.heappush(self.heap, key)
        else:
            if value < self.table[key]:
                self.table[key] = value
                heapq.heappush(self.heap, key)

    def top(self):
        if len(self.heap) > 0:
            key = self.heap[0]
            return self.table[key]
        else:
            return None

    def pop(self):
        key = heapq.heappop(self.heap)
        if self.find(key) is not None:
            value = self.table[key]
            self.table.pop(key)
        else:
            value = None
        return value

    def find(self, key):
        if key in self.table:
            return self.table[key]
        return None

    def __len__(self):
        return len(self.heap)
