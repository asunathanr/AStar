from coord import Coord
from weighted_coord import WeightedCoord
import heapq
import sys

# File: MapGrid.py
# Authors: Kelsey Lewis, Ryan, Nathan Robertson, Pedro Reyes
# Purpose: Describes a MapGrid class used in path finding algorithms.


class MapGrid:
    def __init__(self, xsize: int, ysize: int, obstacles: list):
        self.xsize = xsize
        self.ysize = ysize
        self.gridArea = []
        self.OBSTACLE_VALUE = 2
        self.INVALID_POSITION = -1
        for i in range(0, xsize):
            new = []
            for j in range(0, ysize):
                new.append(1)
            self.gridArea.append(new)
        for coord in obstacles:
            self.gridArea[coord.x][coord.y] = self.OBSTACLE_VALUE

    def cost(self, coord):
        if self.is_valid_coord(coord):
            return self.gridArea[coord.x][coord.y]
        return self.INVALID_POSITION

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
        """
        :param coord1:
        :param coord2:
        :return: True if coord1 is one tile away from coord2, false otherwise
        """
        manhattan_dist = abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)
        if manhattan_dist == 1:
            return True
        return False

    def cell_value(self, coord: Coord):
        if self.is_valid_coord(coord):
            return self.gridArea[coord.x][coord.y]
        return self.INVALID_POSITION

    def neighbors(self, coord: Coord) -> list:
        """
        :param coord:
        :return: All neighbors of coord in a list. (A coord with no neighbors would return empty list)
        """
        make_neighbor = lambda x, y: Coord(coord.x + x, coord.y + y)
        dist = map(lambda i: make_neighbor(i[0], i[1]), [(0, -1), (0, 1), (-1, 0), (1, 0)])
        return list(filter(lambda i: self.is_adjacent(coord, i), dist))

    def insert_obstacle(self, coord: Coord) -> None:
        if self.is_valid_coord(coord):
            self.gridArea[coord.x][coord.y] = self.OBSTACLE_VALUE

    def obstacles(self) -> list:
        li = []
        for i in range(0, self.xsize):
            for j in range(0, self.ysize):
                if self.gridArea[i][j] != 1:
                    li.append(Coord(i, j))
        return li
