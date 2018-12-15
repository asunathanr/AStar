from weighted_coord import WeightedCoord
import unittest


class WeightedCoordTest(unittest.TestCase):
    def test_less_than(self):
        coord1 = WeightedCoord(10, 2, 2)
        coord2 = WeightedCoord(20, 1, 1)
        self.assertTrue(coord1 < coord2)
        self.assertFalse(coord2 < coord1)
