import unittest
from AStar import AStar
from weighted_coord import Coord, WeightedCoord


class SimpleAStarTest(unittest.TestCase):
    def setUp(self):
        self.grid = AStar(2, 2, [])

    def test_invalid_coords(self):
        invalid1 = Coord(-1, -1)
        invalid2 = Coord(5, 5)
        result = self.grid.a_star(invalid1, invalid2)
        self.assertEqual(None, result)

    def test_no_path(self):
        path = set(self.grid.a_star(Coord(0, 0), Coord(0, 0)))
        self.assertEqual(set(), path)

    def test_simple_path(self):
        path = set(self.grid.a_star(Coord(0, 0), Coord(1, 1)))
        self.assertEqual({WeightedCoord(0, 0, 0), WeightedCoord(1, 1, 0), WeightedCoord(0, 1, 1)}, path)


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
