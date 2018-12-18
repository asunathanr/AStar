from PathMaker import *
from MapGrid import print_grid
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
    to generate a file called profiling_result which can be viewed by running the display_stats.py script
"""


def print_path(path: []) -> None:
    list(map(lambda cell: print(str(cell), sep=' '), path))


def make_grid(size: (int, int), obstacle_prob: int) -> PathMaker:
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
    return PathMaker(xsize, ysize, obstacles)


xsize = 10
ysize = 10
grid = make_grid((xsize, ysize), 30)
print(timeit.timeit(lambda: grid.make(Coord(0, 0), Coord(xsize - 1, ysize - 1)), number=1))
path = grid.make(Coord(0, 0), Coord(xsize - 1, ysize - 1))
print_grid(grid, path)
