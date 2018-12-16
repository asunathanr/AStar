import heapq


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
        heapq.heappush(self.heap, (key, value))
        self.table[key] = value

    def pop(self):
        key, value = heapq.heappop(self.heap)
        if self.find(key) is not None:
            value = self.table[key]
            self.table.pop(key)
        return key, value

    def find(self, key):
        if key in self.table:
            return self.table[key]
        return None
