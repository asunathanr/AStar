import unittest
from heuristics import manhattan
from map_grid import MapGrid
from a_star import AStar
from Coordinate.coord import Coord

"""
File: test_astar.py
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
        self.grid = MapGrid(2, 2, [])
        self.astar = AStar(self.grid, manhattan)

    def test_first_cell(self):
        path = self.astar.execute((Coord(0, 0), Coord(0, 0)))
        self.assertEqual([Coord(0, 0)], path)

    def test_last_cell(self):
        path = AStar(self.grid, manhattan).execute((Coord(1, 1), Coord(1, 1)))
        self.assertEqual([Coord(1, 1)], path)


class OffGridTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(2, 2, [])

    def test_below_grid(self):
        path = AStar(self.grid, manhattan).execute((Coord(-1, -1), Coord(-2, -2)))
        self.assertEqual([], path)


class SimpleAStarTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(2, 2, [])
        self.maker = AStar(self.grid, manhattan)

    def test_simple_path(self):
        path = set(self.maker.execute((Coord(0, 0), Coord(1, 1))))
        self.assertEqual({Coord(0, 0), Coord(0, 1), Coord(1, 1)}, path)


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
        self.grid = MapGrid(3, 3, obstacles)

    def test_only_path(self):
        algo = AStar(self.grid, manhattan)
        path = set(algo.execute((Coord(0, 0), Coord(2, 2))))
        coord_path = set(map(lambda cell: Coord(cell.x, cell.y), path))
        self.assertEqual({Coord(0, 0), Coord(1, 0), Coord(1, 1), Coord(1, 2), Coord(2, 2)}, coord_path)

    def test_tricky_path(self):
        tricky_grid = MapGrid(3, 3, [Coord(0, 1), Coord(2, 1)])
        path = set(AStar(tricky_grid, manhattan).execute((Coord(0, 0), Coord(2, 2))))
        coord_path = set(map(lambda cell: Coord(cell.x, cell.y), path))
        self.assertEqual({Coord(0, 0), Coord(1, 0), Coord(1, 1), Coord(1, 2), Coord(2, 2)}, coord_path)


class ComplexPathTest(unittest.TestCase):
    def test_l_wall(self):
        """
        An L-shaped wall is between the start and end.
        Test to see if A* goes around wall instead of walking straight up to it.
        Expected outcome:
        P P P P
        P X X E
        S . X .
        . . X .
        """
        grid = MapGrid(4, 4, [Coord(2, 1), Coord(2, 2), Coord(1, 2), Coord(0, 2)])
        expected_path = {Coord(1, 0), Coord(2, 0), Coord(3, 0), Coord(3, 1), Coord(3, 2), Coord(3, 3), Coord(2, 3)}
        actual_path = AStar(grid, manhattan).execute((Coord(1, 0), Coord(2, 3)))
        self.assertEqual(expected_path, set(actual_path))


class RightToLeftTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(2, 2, [])

    def test_simple_path(self):
        path = set(AStar(self.grid, manhattan).execute((Coord(1, 1), Coord(0, 0))))
        self.assertEqual({Coord(1, 1), Coord(1, 0), Coord(0, 0)}, path)
