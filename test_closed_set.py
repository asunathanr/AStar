from a_star import ClosedSet, Coord, SearchNode
import unittest

"""
File: test_closed_set.py
Author: Nathan Robertson
Purpose: Test behavior of ClosedSet class
"""


class ClosedSetTest(unittest.TestCase):
    def setUp(self):
        self.closed = ClosedSet()

    def test_add(self):
        current = SearchNode(2, (2, 2))
        self.closed.add(current, current.weight)
        self.assertTrue(self.closed.find(current))
