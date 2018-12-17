from coord import Coord
from MapGrid import MapGrid

# https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/


def make_rect(grid: MapGrid, tile: Coord):
    sum_map = MapGrid(grid.xsize, grid.ysize, [])
    for i in range(0, grid.xsize):
        sum_map.gridArea[0][i] = grid.cost(Coord(0, i))
        sum_map.gridArea[i][0] = grid.cost(Coord(i, 0))
    for i in range(1, grid.ysize):
        for j in range(1, grid.xsize):
            if grid.cost(Coord(i, j)) == grid.CELL_VALUE:
                sum_map.gridArea[i][j] = min(sum_map.gridArea[i][j - 1], sum_map.gridArea[i - 1][j], sum_map.gridArea[i - 1][j - 1]) + 1
            else:
                sum_map.gridArea[i][j] = grid.OBSTACLE_VALUE
    max_value = sum_map.cost(Coord(0, 0))
    max_coords = Coord(0, 0)
    for i in range(0, grid.xsize):
        for j in range(0, grid.ysize):
            if sum_map.gridArea[i][j] > max_value:
                max_value = sum_map.gridArea[i][j]
                max_coords = Coord(i, j)
    return Rectangle(max_coords, (max_value, max_value))


class Rectangle:
    def __init__(self, origin, dim):
        self.origin = origin
        self.dim = dim

    def macro_coord(self, start, end):
        pass