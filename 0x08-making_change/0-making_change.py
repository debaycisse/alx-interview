#!/usr/bin/python3
"""This modules house the definiton of a function, named makeChange"""


def makeChange(coins, total):
    """Calculates the minimum number of coins that
    should be added to obtain a given total

    Args:
        coins: a list of given coins
        total: a total number of integer that needs to be obtained

    Returns:
        the minimum number of coins, needed if possible, otherwise 0
    """
    if total == 0:
        return 0
    if len(coins) == 0 or total < 0:
        return -1

    coins.sort()
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
