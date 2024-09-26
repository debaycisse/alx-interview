#!/usr/bin/python3
"""This module houses the implementation of a technical interview,
named island_perimeter, which calculates a number of island in
given 2D (two-dimensional array)"""


def is_valid_array(grid):
    """verifies that a given grid is a nested array of integers

    Args:
        grid - a grid whose contents are verified

    Returns:
        True if the given grid is a nested array of integers, else False
    """
    try:
        num_of_row = len(grid)
        num_of_col = len(grid[0])
        # check all rows have the same number of columns
        i = 0
        while i < num_of_row:
            if (len(grid[i]) != num_of_col):
                return False
            i += 1

        # check all element are either 0 or 1
        for row in grid:
            for element in row:
                if (element != 0 and element != 1):
                    return False
        return True
    except Exception as e:
        return False


def island_perimeter(grid):
    """Calculates the number of island, found inside a given grid

    Args:
        grid - a grid whose total number of contained island is calculated

    Returns:
        The total number of island, found in a given grid
    """
    if (not is_valid_array(grid)):
        return 0
    num_of_island = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                num_of_island += 4
                if (col > 0) and (grid[row][col - 1] > 0):
                    num_of_island -= 2
                if (row > 0) and (grid[row - 1][col] > 0):
                    num_of_island -= 2
    return num_of_island
