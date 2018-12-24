from map_grid import MapGrid, print_grid
from diagonal_grid import DiagonalGrid, print_diagonal
from heuristics import diagonal_tie_breaker, tie_breaker_h
from helpers import *
# My A* implementation
from a_star import *
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
    Update:
        I managed to meet the above goal (100x100 grid in <= 0.05 seconds). 
        Now I think the next efficency goals are to be split into two parts.
        1. Get the average timing to be in range 1 ms <= n < 10 ms  for a 100x100 grid.
        2. Find 100 randomly generated paths on a grid in < 1 second.
    
    Run in terminal with command: python -m cProfile -o profiling_results astar_timing.py
    to generate a file called profiling_results which can be viewed by running the display_stats.py script
"""


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
                obstacles.append(Coord(i, j))
    return DiagonalGrid(xsize, ysize, obstacles)


def find_path(graph, endpoints, heuristic):
    return AStar(graph, heuristic).execute(endpoints)


times = [1, 10, 100]


def print_result(result):
    for t, r in zip(times, result):
        print("Processed: ", t, " paths. The min processing time was: ", min(r))


xsize = 50
ysize = 50

obstacle_prob = [1, 10, 20, 50]
grid = make_diagonal_grid((xsize, ysize), 8)
top_left = Coord(0, 0)
bottom_right = Coord(xsize - 1, ysize - 1)

if __name__ == "__main__":
    print(timeit.timeit(lambda: AStar(grid, diagonal_tie_breaker).execute((top_left, bottom_right)), number=1000))
else:
    for i in range(0, 100):
        AStar(grid, diagonal_tie_breaker).execute((top_left, bottom_right))
