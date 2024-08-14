#!/usr/bin/python3
"""2Dmatrix rotate Module"""


def rotate_2d_matrix(matrix):
    """method rotates a 2dmatrix 90°
    param: a 2d matrix"""
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
