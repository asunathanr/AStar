from Coordinate.coord import Coord


"""
File: helpers.py
Author: Nathan Robertson
A collection of useful helper functions.
"""


def flatten(li: []) -> []:
    """
    https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
    :param li:
    :return: flattened li
    """
    return [item for sublist in li for item in sublist]


def was_solution_found(endpoints: (Coord, Coord), tentative_path: []) -> bool:
    """
    :param endpoints: A tuple containing start and goal coordinates
    :param tentative_path: list of coordinates to check for start and goal.
    :return: If path is a path from start to goal.
    """
    start, goal = endpoints
    return start in tentative_path and goal in tentative_path
