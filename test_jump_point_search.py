import unittest
from coord import Coord
from diagonal_grid import DiagonalGrid
from jps_node import JPSNode
from jump_point_search import JumpPointSearch
from heuristics import diagonal_tie_breaker


"""
File: test_jump_point_search.py
Author: Nathan Robertson
Purpose: Test if jump point search can correctly find minimum path on a diagonal grid.
"""


class TestJumpPointSearch(unittest.TestCase):
    def setUp(self):
        self.grid = DiagonalGrid(4, 4, [])
        self.jps = JumpPointSearch(self.grid, diagonal_tie_breaker)

    def test_jump(self):
        expected_coord = Coord(0, 3)
        coord = self.jps.jump((0, 0), (0, 1), (0, 0), expected_coord)
        self.assertEqual(expected_coord, coord)

    def test_diagonal_jump(self):
        expected_coord = Coord(3, 3)
        coord = self.jps.jump((0, 0), (1, 1), (0, 0), expected_coord)
        self.assertEqual(expected_coord, coord)

    def test_prune_start_node(self):
        expected = {Coord(0, 1)}
        current = JPSNode(Coord(0, 0), Coord(0, 1))
        neighbors = set(self.jps.prune(current))
        self.assertEqual(expected, neighbors)

    def test_execute(self):
        expected = [Coord(0, 0), Coord(3, 3)]
        path = list(map(lambda jump_point: jump_point.coord, self.jps.execute((Coord(0, 0), Coord(3, 3)))))
        self.assertEqual(expected, path)

    def test_horizontal_execute(self):
        expected = [Coord(0, 0), Coord(0, 3)]
        path = list(map(lambda jump_point: jump_point.coord, self.jps.execute((Coord(0, 0), Coord(0, 3)))))
        self.assertEqual(expected, path)


class ConnectJumpPointsTest(unittest.TestCase):
    def setUp(self):
        self.grid = DiagonalGrid(4, 4, [])
        self.jps = JumpPointSearch(self.grid, diagonal_tie_breaker)

    def test_full_horizontal_path(self):
        expected = [Coord(0, 0), Coord(0, 1), Coord(0, 2), Coord(0, 3)]
        path = self.jps.execute((Coord(0, 0), Coord(0, 3)))
        self.assertEqual(expected, self.jps.connect_path(path))

    def test_full_diagonal_path(self):
        expected = [Coord(0, 0), Coord(1, 1), Coord(2, 2), Coord(3, 3)]
        path = self.jps.execute((Coord(0, 0), Coord(3, 3)))
        self.assertEqual(expected, self.jps.connect_path(path))

    def test_obstacle_execute(self):
        obstacle_grid = DiagonalGrid(4, 4, [Coord(0, 2)])
        expected = [Coord(0, 0), Coord(0, 1), Coord(1, 0)]
