from MapGrid import MapGrid, print_grid
from DiagonalGrid import DiagonalGrid, print_diagonal
from heuristics import diagonal_tie_breaker, tie_breaker_h
# My A* implementation
from a_star import *
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


xsize = 100
ysize = 100
grid = make_grid((xsize, ysize), 10)
diagonal_grid = make_diagonal_grid((xsize, ysize), 10)
print(timeit.timeit(lambda: AStar(grid, tie_breaker_h).execute((Coord(0, 0), Coord(xsize - 1, ysize - 1))), number=1))
print(timeit.timeit(lambda: AStar(diagonal_grid, diagonal_tie_breaker).execute((Coord(0, 0), Coord(xsize - 1, ysize - 1))), number=1))
#print(timeit.timeit(lambda: astar.find_path(Coord(0, 0), Coord(xsize - 1, ysize - 1), grid.neighbors, heuristic_cost_estimate_fnct=tie_breaker_h), number=1))
path = AStar(diagonal_grid, tie_breaker_h).execute((Coord(0, 0), Coord(xsize - 1, ysize - 1)))
print_diagonal(diagonal_grid, path)
