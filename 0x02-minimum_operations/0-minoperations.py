#!/usr/bin/python3
"""This module houses the definition of functions that are used to
calculates the fewest number of operations needed to take place
for the H to copied in a given number times"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number operation, needed to result in having
    letter H in n times. The just two operations are Copy All and Paste

    Args:
        n - the number of times to have letter 'H' endup in

    Returns:
        the number of fewest operations needed to place
    """
    num = n
    data = ['H']
    copied = ''
    op_count = 0
    divisor = 0
    try:
        while (len(data[0]) < num):
            divisor = len(data[0])
            if (num % divisor == 0):
                op_count += 2
                copied = data[0]
                data[0] += copied
            else:
                op_count += 1
                data[0] += copied
    except Exception:
        pass
    if (len(data[0]) != n):
        return 0
    return op_count
