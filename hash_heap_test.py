from HashHeap import HashHeap
import unittest

"""
File: HashHeapTest
Author: Nathan Robertson
Purpose:
    Test the combined hash table/heap data structure.
    Invariant:
    1. pop will return lowest value if one exists
    2. add will add item to both hash table and push it onto heap
    3. If item already in hash table will simply replace that items value.
"""


class HashHeapTest(unittest.TestCase):
    def setUp(self):
        self.hash_heap = HashHeap()

    def test_add_item(self):
        """
        Add item to heap and find it later
        :return:
        """
        self.hash_heap.add(1, 2)
        self.assertEqual(2, self.hash_heap.find(1))

    def test_pop(self):
        self.hash_heap.add(1, 2)
        value = self.hash_heap.pop()
        self.assertEqual(2, value)
        self.assertIsNone(self.hash_heap.find(1))

    def test_min_prop(self):
        """
        Test min heap property that smallest item is first to come off.
        :return:
        """
        self.hash_heap.add(1, 2)
        self.hash_heap.add(3, 4)
        value = self.hash_heap.top()
        self.assertEqual(2, value)
