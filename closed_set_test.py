from a_star import ClosedSet, Coord, WeightedCoord
import unittest


class ClosedSetTest(unittest.TestCase):
    def setUp(self):
        self.closed = ClosedSet()

    def test_add(self):
        current = WeightedCoord(2, 3, 3)
        self.closed.add(current, current.weight)
        self.assertTrue(self.closed.find(current))

    def test_filter_neighbor(self):
        self.closed.add(Coord(1, 2), 3)
        neighbors = [Coord(1, 2), Coord(3, 4)]
        for i in neighbors:
            self.closed.filter_neighbor(1, i)
        self.assertFalse(self.closed.find(Coord(1, 2)))

    def test_leave_neighbor_alone(self):
        self.closed.add(Coord(1, 2), 1)
        neighbors = [Coord(1, 2), Coord(3, 4)]
        for i in neighbors:
            self.closed.filter_neighbor(3, i)
        self.assertTrue(self.closed.find(Coord(1, 2)))
