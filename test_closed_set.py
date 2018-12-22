from a_star import ClosedSet, Coord, SearchNode
import unittest


class ClosedSetTest(unittest.TestCase):
    def setUp(self):
        self.closed = ClosedSet()

    def test_add(self):
        current = SearchNode(2, (2, 2))
        self.closed.add(current, current.weight)
        self.assertTrue(self.closed.find(current))
