from AStar.hash_heap import HashHeap
from AStar.a_star import Coord, SearchNode
import unittest

"""
File: HashHeapTest
Author: Nathan Robertson
Purpose:
    Test the combined hash table/heap data structure.
    Invariant:
    1. heap[0] should always contain the lowest node.
    2. table's keys will be the location of the node. For instance (0, 0) if using grid notation
"""


class HashHeapTest(unittest.TestCase):
    def setUp(self):
        self.search_node = SearchNode(2, Coord(1, 1))
        self.lower_search_node = SearchNode(1, Coord(1, 1))
        self.hash_heap = HashHeap()

    def test_add_item(self):
        """
        Add item to heap and find it later
        :return:
        """
        self.hash_heap.add(self.search_node)
        self.assertEqual(self.search_node, self.hash_heap.find(self.search_node.value))

    def test_pop(self):
        self.hash_heap.add(self.search_node)
        value = self.hash_heap.pop()
        self.assertEqual(self.search_node, value)
        self.assertIsNone(self.hash_heap.find(self.search_node.value))

    def test_min_prop(self):
        """
        Test min heap property that smallest item is first to come off.
        :return:
        """
        self.hash_heap.add(self.search_node)
        self.hash_heap.add(self.lower_search_node)
        value = self.hash_heap.top()
        self.assertEqual(self.lower_search_node, value)
