#!/usr/bin/python3
"""This module houses the implementation
of function, named rotate_2d_matrix"""


def transpose_matrix(matrix):
    """Transposes a given 2D matrix in-place.

    Args:
    matrix: The given matrix to be transposed.
    """
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


def rotate_matrix(matrix):
    """Rotates a given 2D matrix in place

    Args:
        matrix - the given matrix to be rotated in 90 degrees
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """Rotates a given matrix by 90 degrees in an in-place manner.
    A given matrix is modified to have it in a 90 degress rotated form

    Args:
        matrix - the given matrix to be rotated
    """
    transpose_matrix(matrix)
    rotate_matrix(matrix)
