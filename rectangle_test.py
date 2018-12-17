from rectangle import *
import unittest


class FillEmptyGridTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(3, 3, [])
        self.rect = make_rect(self.grid, Coord(0, 0))

    def test_origin(self):
        self.assertEqual(Coord(0, 0), self.rect.origin)

    def test_fill(self):
        self.assertEqual(3, self.rect.dim[0])
        self.assertEqual(3, self.rect.dim[1])


class FillObstacleGridTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(3, 3, [Coord(1, 0), Coord(1, 1), Coord(1, 2)])
        self.rect = make_rect(self.grid, Coord(0, 0))

    def test_origin(self):
        self.assertEqual(Coord(0, 0), self.rect.origin)

    def test_fill(self):
        self.assertEqual(1, self.rect.dim[0])
        self.assertEqual(3, self.rect.dim[0])