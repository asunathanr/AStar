from MapGrid import *
import queue


class BfsNode:
    def __init__(self, coord, parent):
        self.coord = coord
        self.parent = parent


def bfs(grid: MapGrid, start: Coord, end: Coord):
    frontier = queue.Queue()
    frontier.put(start)
    visited = {start: True}
    while not frontier.empty():
        current = frontier.get()
        for next_node in grid.neighbors(current):
            if next_node not in visited:
                frontier.put(next_node)
                visited[next_node] = True
