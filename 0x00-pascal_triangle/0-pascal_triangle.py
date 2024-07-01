#!/usr/bin/python3
"""The pascals triangle module"""


def pascal_triangle(n):
    """
    This algorithm builds a pascals triangle n times
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        for i in range(n):
            # begin with a row of ones
            row = [1] * (i + 1)

            # Fill other values
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            # join row to the ptriangle
            triangle.append(row)
        return triangle


if __name__ == "__main__":  # Main function
    """
    main tests n=5
    """
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
