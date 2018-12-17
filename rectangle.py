from coord import Coord
from MapGrid import MapGrid

# https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
# https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/


def find_maximal_rectangles(grid: MapGrid):
    sum_map = make_sum_matrix(grid)
    return make_rect(grid, sum_map)


def make_rect(grid: MapGrid, sums: [], prev_rect=None):
    """
    @todo is square currently make it rectangle
    :param grid:
    :return:
    """
    sum_map = make_sum_matrix(sums)
    if prev_rect is None:
        max_value = sum_map[0][0]
    else:
        max_value = prev_rect.dim[0]
    max_coords = Coord(0, 0)
    for i in range(0, grid.xsize):
        for j in range(0, grid.ysize):
            if sum_map[i][j] > max_value:
                max_value = sum_map[i][j]
                max_coords = Coord(i, j)
    return Rectangle(max_coords, (max_value, max_value))


def make_sum_matrix(grid: MapGrid):
    bin_values = to_binary_matrix(grid)
    sum_matrix = init_matrix((grid.xsize, grid.ysize))
    for i in range(0, grid.xsize):
        sum_matrix[0][i] = bin_values[0][i]
        sum_matrix[i][0] = bin_values[i][0]
    for i in range(1, grid.ysize):
        for j in range(1, grid.xsize):
            if bin_values[i][j] == 1:
                sum_matrix[i][j] = min(sum_matrix[i][j - 1], sum_matrix[i - 1][j], sum_matrix[i - 1][j - 1]) + 1
            else:
                sum_matrix[i][j] = 0
    return sum_matrix


def init_matrix(dim):
    matrix = []
    rows, cols = dim
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            row.append(0)
        matrix.append(row)
    return matrix


def to_binary_matrix(grid: MapGrid) -> []:
    """
    Converts grid of cells to 2D List which is equivalent to a binary matrix
    :param grid:
    :return: 2D Binary Matrix
    """
    matrix = []
    for i in range(0, grid.xsize):
        row = []
        for j in range(0, grid.ysize):
            if grid.cost(Coord(i, j)) == grid.CELL_VALUE:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


class Rectangle:
    def __init__(self, origin, dim):
        self.origin = origin
        self.dim = dim

    def macro_coord(self, start, end):
        pass