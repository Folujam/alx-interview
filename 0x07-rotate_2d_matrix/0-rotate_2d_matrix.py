#!/usr/bin/python3
"""2d Matrix rotate Module"""


def rotate_2d_matrix(matrix):
    """rotates a 2d-matrix 90° counter
      clock-wise in-place
      param: takes a matrix"""
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
