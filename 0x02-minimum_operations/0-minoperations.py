#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """gets fewest n of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    opr, defNum = 0, 2
    while defNum <= n:
        # if n evenly divides by defNum
        if n % defNum == 0:
            # total even-divisions by defNum = total operations
            opr += defNum
            # set n to the remainder
            n = n / defNum
            # reduce defNum to find remaining smaller vals that evenly-divide n
            defNum -= 1
        # increment defNum until it evenly-divides n
        defNum += 1
    return opr
