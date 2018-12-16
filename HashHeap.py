import heapq


class HashHeap:
    """
    A structure which allows both fast search and fast heaping.
    Found this idea at: https://github.com/jonasnick/A-star/blob/master/astar/datastructures/HashPriorityQueue.java
    """
    def __init__(self):
        self.heap = []
        self.table = {}

    def add(self, key, value):
        heapq.heappush(self.heap, (key, value))
        self.table[key] = value

    def remove(self, key):
        pass

    def pop(self):
        return heapq.heappop(self.heap)

    def find(self, key):
        if key in self.table:
            return self.table[key]
        return None
