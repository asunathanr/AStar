from PathMaker import *
from MapGrid import MapGrid, manhattan, print_grid
from DiagonalGrid import DiagonalGrid, diagonal, print_diagonal
from functools import lru_cache
# My A* implementation
from a_star import AStar
# Another A* implementation
import astar
import timeit
import random


"""
File: astar_timing.py
Author: Nathan Robertson
Purpose:
    Investigate efficiency of astar algorithm implementation.
    Battlecode 2017's map took place on maps ranging from size 20x20 to 50x50. 
    Therefore the next order of magnitude is 100x100.
    The max time given was 10 seconds with 0.05 seconds added each round. 
    I will start with trying to get a 100x100 in under 10 seconds then progressively decrease the time.
    The current goal is to get it to run 100x100 grids with obstacles in <= 0.05 second
    
    Run in terminal with command: python -m cProfile -o profiling_results astar_timing.py
    to generate a file called profiling_results which can be viewed by running the display_stats.py script
"""


@lru_cache(maxsize=None)
def tie_breaker_h(coord1, coord2):
    """
    Decorator heuristic which adds a tie breaker to the formula.
    Try to adjust the heuristic to favor certain tiles even if cost is the same.
    :param coord1:
    :param coord2:
    :return:
    """
    return manhattan(coord1, coord2) * (1.0 + 1/1000)


@lru_cache(maxsize=None)
def diagonal_tie_breaker(coord1, coord2):
    return diagonal(coord1, coord2) * (1.0 + 1 / 1000)


def make_grid(size: (int, int), obstacle_prob: int) -> MapGrid:
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
                if i != j:
                    obstacles.append(Coord(i, j))
    return MapGrid(xsize, ysize, obstacles)


def make_diagonal_grid(size: (int, int), obstacle_prob: int) -> DiagonalGrid:
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
                if i != j:
                    obstacles.append(Coord(i, j))
    return DiagonalGrid(xsize, ysize, obstacles)


xsize = 50
ysize = 50
grid = make_grid((xsize, ysize), 10)
diagonal_grid = make_diagonal_grid((xsize, ysize), 10)
print(timeit.timeit(lambda: AStar(grid, (Coord(0, 0), Coord(xsize - 1, ysize - 1)), tie_breaker_h).execute(), number=1))
print(timeit.timeit(lambda: AStar(diagonal_grid, (Coord(0, 0), Coord(xsize - 1, ysize - 1)), diagonal_tie_breaker).execute(), number=1))
#print(timeit.timeit(lambda: astar.find_path(Coord(0, 0), Coord(xsize - 1, ysize - 1), grid.neighbors, heuristic_cost_estimate_fnct=tie_breaker_h), number=1))
path = AStar(diagonal_grid, (Coord(0, 0), Coord(xsize - 1, ysize - 1)), tie_breaker_h).execute()
print_diagonal(diagonal_grid, path)
