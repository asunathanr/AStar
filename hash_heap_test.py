from HashHeap import HashHeap
from a_star import Coord, SearchNode
import unittest

"""
File: HashHeapTest
Author: Nathan Robertson
Purpose:
    Test the combined hash table/heap data structure.
    Invariant:
    1. pop will return lowest value if one exists
    2. add will add/update item in hash table and push it onto heap
    3. If item is already in the hash table it will simply replace that items value.
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

    def test_should_update(self):
        self.hash_heap.add(self.search_node)
        self.assertTrue(self.hash_heap.should_update(SearchNode(2, (1, 2))))
