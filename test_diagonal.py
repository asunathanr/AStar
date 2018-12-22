from DiagonalGrid import DiagonalGrid, diagonal
from coord import Coord
import unittest


"""
File: test_diagonal.py
Author: Nathan Robertson
Purpose: Test behavior of DiagonalGrid class
"""


class DiagonalGridTest(unittest.TestCase):
    def setUp(self):
        self.grid = DiagonalGrid(3, 3, [])

    def test_neighbors(self):
        coord = Coord(1, 1)
        neighbors = set(self.grid.neighbors(coord))
        self.assertEqual({Coord(0, 0), Coord(0, 1), Coord(1, 0), Coord(2, 1), Coord(2, 2), Coord(0, 2), Coord(2, 0), Coord(1, 2)}, neighbors)

    def test_is_adjacent(self):
        self.assertFalse(self.grid.is_adjacent(Coord(0, 0), Coord(0, 0)))
        self.assertFalse(self.grid.is_adjacent(Coord(0, 0), Coord(1, 2)))
        self.assertFalse(self.grid.is_adjacent(Coord(-1, 0), Coord(1, 2)))
        self.assertFalse(self.grid.is_adjacent(Coord(-1, 0), Coord(-1, 2)))

        self.assertTrue(self.grid.is_adjacent(Coord(0, 0), Coord(0, 1)))
        self.assertTrue(self.grid.is_adjacent(Coord(1, 1), Coord(0, 1)))
        self.assertTrue(self.grid.is_adjacent(Coord(0, 0), Coord(1, 1)))