from coord import Coord

# File: MapGrid.py
# Authors: Kelsey Lewis, Ryan, Nathan Robertson, Pedro Reyes
# Purpose: Describes a MapGrid class used in path finding algorithms.


class MapGrid:
    def __init__(self, xsize: int, ysize: int, coords: list):
        self.xsize = xsize
        self.ysize = ysize
        self.gridArea = []
        for i in range(0, xsize):
            new = []
            for j in range(0, ysize):
                new.append(0)
            self.gridArea.append(new)

    def is_adjacent(self, coord1: Coord, coord2: Coord) -> bool:
        """
        Is coordinate one adjacent to coordinate 2?
        TODO: Do we count coord1 == coord2 as being adjacent?
        """
        if self.is_valid_coord(coord1) and self.is_valid_coord(coord2):
            if self.is_adjacent_position(coord1, coord2):
                return True
        return False

    def is_valid_coord(self, coord: Coord) -> bool:
        """
        :param coord:
        :return: If coordinate is in gridArea
        """
        if coord.x < 0:
            return False
        if coord.y < 0:
            return False
        if coord.x >= self.xsize:
            return False
        if coord.y >= self.ysize:
            return False
        return True

    def is_adjacent_position(self, coord1: Coord, coord2: Coord) -> bool:
        manhattan_dist = abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)
        if manhattan_dist == 1:
            return True
        return False

    def neighbors(self, coord: Coord) -> list:
        """
        :param coord:
        :return: All neighbors of coord in a list. (A coord with no neighbors would return empty list)
        """
        raw_neighbors = [
            Coord(coord.x, coord.y + 1),
            Coord(coord.x, coord.y - 1),
            Coord(coord.x - 1, coord.y),
            Coord(coord.x + 1, coord.y)
        ]
        valid_neighbors = []
        for i in raw_neighbors:
            if self.is_adjacent(coord, i):
                valid_neighbors.append(i)
        return valid_neighbors

    def insert_obstacle(self, coord: Coord) -> None:
        if self.is_valid_coord(coord):
            self.gridArea[coord.x][coord.y] = 1

    def obstacles(self) -> list:
        li = []
        for i in range(0, self.xsize):
            for j in range(0, self.ysize):
                if self.gridArea[i][j] != 0:
                    li.append(Coord(i, j))
        return li

