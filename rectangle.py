from coord import Coord
from MapGrid import MapGrid


def make_rect(grid: MapGrid, tile: Coord):
    new_x = grid.xsize
    new_y = grid.ysize
    i = tile.x
    next_tile = tile
    neighbors = grid.neighbors(tile)

    return Rectangle(tile, (new_x, new_y))


def make_column(grid: MapGrid, tile: Coord):
    column = []
    for i in range(0, grid.xsize):
        column.append(Coord(i, tile.y))
    return list(filter(lambda curr_tile: curr_tile not in grid.obstacles(), column))


def check_column(grid: MapGrid, tile: Coord) -> bool:
    for obstacle in grid.obstacles():
        if obstacle.y == tile.y:
            return False
    return True


def up(coord: Coord):
    return Coord(coord.x, coord.y + 1)


def right(coord: Coord):
    return Coord(coord.x + 1, coord.y)


class Rectangle:
    def __init__(self, origin, dim):
        self.origin = origin
        self.dim = dim

    def macro_coord(self, start, end):
        pass