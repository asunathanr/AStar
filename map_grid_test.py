import unittest
from MapGrid import *
from AStar import AStar
from coord import Coord


# File: map_grid_test.py
# Authors: Jason Cassimus, Eric Day, Nathan Robertson
# Purpose: Test the MapGrid class.


class GridTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(3, 3, [])

    def test_is_adjacent(self):
        self.assertFalse(self.grid.is_adjacent(Coord(0, 0), Coord(0, 0)))
        self.assertFalse(self.grid.is_adjacent(Coord(0, 0), Coord(1, 2)))
        self.assertFalse(self.grid.is_adjacent(Coord(-1, 0), Coord(1, 2)))
        self.assertFalse(self.grid.is_adjacent(Coord(-1, 0), Coord(-1, 2)))

        self.assertTrue(self.grid.is_adjacent(Coord(0, 0), Coord(0, 1)))
        self.assertTrue(self.grid.is_adjacent(Coord(1, 1), Coord(0, 1)))

    def test_neighbors(self):
        neighbors = self.grid.neighbors(Coord(1, 1))
        expected = {Coord(1, 2), Coord(0, 1), Coord(2, 1), Coord(1, 0)}
        self.assertEqual(expected, set(neighbors))

    def test_out_of_bound_neighbors(self):
        neighbors = self.grid.neighbors(Coord(0, -1))
        self.assertEqual(set(), set(neighbors), "Expected coords not equivalent to actual coords.")


class ObstacleGridTest(unittest.TestCase):
    """
    Test obstacle mechanism in MapGrid
    """
    def setUp(self):
        self.grid = MapGrid(3, 3, [])
        self.obstacle_grid = MapGrid(3, 3, [Coord(1, 1), Coord(0, 1)])

    def test_add_obstacle(self):
        self.grid.insert_obstacle(Coord(1, 1))
        self.assertEqual([Coord(1, 1)], self.grid.obstacles())


class AStarTest(unittest.TestCase):
    def setUp(self):
        self.grid = AStar(3, 3, [])

    def test_initialize(self):
        open_set, closed_set = self.grid.initialize(Coord(1, 1))
        self.assertEqual({WeightedCoord(0, 1, 1)}, open_set)
        self.assertEqual(set(), closed_set)

    def test_invalid_coords(self):
        invalid1 = Coord(-1, -1)
        invalid2 = Coord(5, 5)
        result = self.grid.a_star(invalid1, invalid2)
        self.assertEqual(None, result)

    def test_simple_path(self):
        path = self.grid.a_star(Coord(0, 0), Coord(2, 2))
        self.assertEqual({Coord(0, 0), Coord(1, 1), Coord(2, 2)}, path)

    def test_pick_current(self):
        current = self.grid.pick_current({WeightedCoord(1, 1, 1), WeightedCoord(2, 2, 2)})
        self.assertEqual(WeightedCoord(1, 1, 1), current)
