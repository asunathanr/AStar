import unittest
from MapGrid import MapGrid
from a_star import AStar
from PathMaker import PathMaker
from weighted_coord import Coord

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


def manhattan(coord1, coord2):
    return abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)


class SameStartEndTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(2, 2, [])
        self.astar = AStar(self.grid, (Coord(0, 0), Coord(0, 0)), manhattan)
        self.maker = PathMaker(self.grid)

    def test_first_cell(self):
        path = self.astar.execute()
        self.assertEqual([Coord(0, 0)], path)

    def test_last_cell(self):
        path = AStar(self.grid, (Coord(1, 1), Coord(1, 1)), manhattan).execute()
        self.assertEqual([Coord(1, 1)], path)


class OffGridTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(2, 2, [])
        self.maker = PathMaker(self.grid)

    def test_below_grid(self):
        path = self.maker.make(AStar(self.grid, (Coord(-1, -1), Coord(-2, -2)), manhattan))
        self.assertEqual(self.maker.PATH_OUT_OF_BOUNDS, path)


class SimpleAStarTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(2, 2, [])
        self.maker = AStar(self.grid, (Coord(0, 0), Coord(1, 1)), manhattan)

    def test_simple_path(self):
        path = set(self.maker.execute())
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
        self.maker = PathMaker(MapGrid(3, 3, obstacles))

    def test_only_path(self):
        algo = AStar(self.grid, (Coord(0, 0), Coord(2, 2)), manhattan)
        path = set(self.maker.make(algo))
        coord_path = set(map(lambda cell: Coord(cell.x, cell.y), path))
        self.assertEqual({Coord(0, 0), Coord(1, 0), Coord(1, 1), Coord(1, 2), Coord(2, 2)}, coord_path)

    def test_tricky_path(self):
        tricky_grid = MapGrid(3, 3, [Coord(0, 1), Coord(2, 1)])
        maker = PathMaker(tricky_grid)
        path = set(maker.make(AStar(tricky_grid, (Coord(0, 0), Coord(2, 2)), manhattan)))
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
        maker = PathMaker(grid)
        expected_path = {Coord(1, 0), Coord(2, 0), Coord(3, 0), Coord(3, 1), Coord(3, 2), Coord(3, 3), Coord(2, 3)}
        actual_path = maker.make(AStar(grid, (Coord(1, 0), Coord(2, 3)), manhattan))
        self.assertEqual(expected_path, set(actual_path))


class RightToLeftTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(2, 2, [])
        self.maker = PathMaker(self.grid)

    def test_simple_path(self):
        path = set(self.maker.make(AStar(self.grid, (Coord(1, 1), Coord(0, 0)), manhattan)))
        self.assertEqual({Coord(1, 1), Coord(1, 0), Coord(0, 0)}, path)
