from DiagonalGrid import DiagonalGrid, diagonal
from coord import Coord
import unittest


class DiagonalGridTest(unittest.TestCase):
    def setUp(self):
        self.grid = DiagonalGrid(3, 3, [])

    def test_neighbors(self):
        coord = Coord(0, 0)
        neighbors = self.grid.neighbors(coord)
        self.assertEqual([Coord(0, 1), Coord(1, 0), Coord(1, 1)], neighbors)