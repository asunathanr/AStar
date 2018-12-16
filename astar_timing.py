from AStar import *
import timeit
import random


"""
File: astar_timing.py
Author: Nathan Robertson
Purpose:
    Investigate efficiency of astar algorithm implementation.
"""


def print_path(path: []) -> None:
    list(map(lambda cell: print(str(cell), sep=' '), path))


def make_grid(size: (int, int), obstacle_prob: int) -> AStar:
    """
    :param size: tuple of max x and max y values
    :param obstacle_prob: Probability that an obstacle is on a tile.
    :return: AStar grid with randomly generated obstacles
    """
    obstacles = []
    xsize, ysize = size
    for i in range(0, xsize):
        for j in range(0, ysize):
            if random.randint(0, 100) < obstacle_prob:
                obstacles.append(Coord(i, j))
    return AStar(xsize, ysize, obstacles)


xsize = 7
ysize = 7
grid = make_grid((xsize, ysize), 5)

print(timeit.timeit(lambda: grid.a_star(Coord(0, 0), Coord(xsize - 1, ysize - 1)), number=1))

