#!/usr/bin/python3
"""This modules house the definiton of a function, named makeChange"""


def makeChange(coins, total):
    """Calculates the minimum number of coins that
    should be added to obtain a given total

    Args:
        coins - a list of given coins
        total - a total number of integer that needs to be obtained

    Returns:
        the minimum number of coins, needed if possible, otherwise 0
    """
    if total = 0:
        return 0
    if len(coins) == 0 && total > 0:
        return -1
    coins.sort()
    if total - coins[-1] >= 0:
        return 1
    return makeChange(coins, total) + makeChange(coins[:-1], total - coins[-1])

