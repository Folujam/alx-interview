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
                # Get the two numbers from the previous row
                left_num = triangle[i - 1][j - 1]
                right_num = triangle[i - 1][j]

                # Add them together to get the new number
                new_num = left_num + right_num

                # Update the current position in the row with the new number
                row[j] = new_num

            # Add the completed row to the triangle
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
