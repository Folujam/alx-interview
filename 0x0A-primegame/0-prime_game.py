#!/usr/bin/python3
"""prime game Module"""


# pool of integers: 1-n
# rounds of play: x
def isWinner(x, nums):
    """determines a winner in a game of primes"""
    if nums is None or x <= 0:
        return None
    if len(nums) != x:
        return None
    
    ben, maria = 0, 0
    