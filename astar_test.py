import unittest
from AStar import AStar
from weighted_coord import Coord, WeightedCoord

"""
File: astar_test.py
Authors: Nathan Robertson
Purpose: 
    Ensure the AStar path-finding class works correctly.
    Special cases for the A* algorithm:
    1. If a start and end are the same the path given back is an empty list.
    2. If start and end cells are off the grid it should return a special out of bounds value
    3. If an end cell is unreachable from the start cell it should return a special value indicating that.
    
    Normal behavior:
    1. Will return a list of nodes ordered by which nodes to visit first.
    2. First node in list is start node
    3. Last node will be end node.
"""


class SameStartEndTest(unittest.TestCase):
    def setUp(self):
        self.grid = AStar(2, 2, [])

    def test_first_cell(self):
        path = set(self.grid.a_star(Coord(0, 0), Coord(0, 0)))
        self.assertEqual(set(), path)


class OffGridTest(unittest.TestCase):
    def setUp(self):
        self.grid = AStar(3, 3, [])

    def test_below_grid(self):
        path = self.grid.a_star(Coord(-1, -1), Coord(-2, -2))
        self.assertEqual(self.grid.PATH_OUT_OF_BOUNDS, path)


class SimpleAStarTest(unittest.TestCase):
    def setUp(self):
        self.grid = AStar(2, 2, [])

    def test_invalid_coords(self):
        invalid1 = Coord(-1, -1)
        invalid2 = Coord(5, 5)
        result = self.grid.a_star(invalid1, invalid2)
        self.assertEqual(self.grid.PATH_OUT_OF_BOUNDS, result)

    def test_simple_path(self):
        path = set(self.grid.a_star(Coord(0, 0), Coord(1, 1)))
        self.assertEqual({WeightedCoord(0, 0, 0), WeightedCoord(1, 0, 1), WeightedCoord(0, 1, 1)}, path)


class ThreeGridAStarTest(unittest.TestCase):
    """
    Only one path goes through this three by three grid.
    test_path method should give us back this one path.
    It looks like:
    |X|X|E|
    | | | |
    |S|X|X|
    """
    def setUp(self):
        obstacles = [Coord(2, 0), Coord(2, 1), Coord(0, 1), Coord(0, 2)]
        self.grid = AStar(3, 3, obstacles)

    def test_only_path(self):
        path = set(self.grid.a_star(Coord(0, 0), Coord(2, 2)))
        coord_path = set(map(lambda cell: Coord(cell.x, cell.y), path))
        self.assertEqual({Coord(0, 0), Coord(1, 0), Coord(1, 1), Coord(1, 2), Coord(2, 2)}, coord_path)

    def test_tricky_path(self):
        tricky_grid = AStar(3, 3, [Coord(0, 1), Coord(2, 1)])
        path = set(tricky_grid.a_star(Coord(0, 0), Coord(2, 2)))
        coord_path = set(map(lambda cell: Coord(cell.x, cell.y), path))
        self.assertEqual({Coord(0, 0), Coord(1, 0), Coord(1, 1), Coord(1, 2), Coord(2, 2)}, coord_path)
