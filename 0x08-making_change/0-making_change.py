#!/usr/bin/python3
"""thechange Module"""


def makeChange(coins, total):
    """method determines the least amt of coins needed
    to make change
    1. Initialize a list dp with total + 1 elements,
    all set to infinity, except dp[0] = 0.
    2. Iterate over each coin value.
    3. For each coin, iterate from the coin value to the total amount.
    4. Update dp[i] with the minimum number of coins needed to make
    amount i by choosing the minimum between the current value and
    dp[i - coin] + 1.
    5. Return dp[total] if it's not infinity; otherwise, return -1.

    This solution has a runtime of O(total * len(coins)),
    making it efficient for large inputs.
    """
    # coins: a list of values of coins in possession
    # Create a list to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount

    # Iterate over each coin value
    for coin in coins:
        # Iterate from the coin value to the total amount
        for i in range(coin, total + 1):
            # Update the minimum number of coins for the current amount
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the minimum number of coins for the total amount
    return dp[total] if dp[total] != float('inf') else -1
