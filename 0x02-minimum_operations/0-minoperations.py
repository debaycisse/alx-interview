#!/usr/bin/env python3
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
    op_count = [0]
    content = ['H']

    def find_div(num: int) -> int:
        """
        Finds the highest divisor for the given number

        Args:
            num - the number whose highest divisor is to be obtained

        Returns:
            the (highest) number among the possible divisors
        """
        i = 2
        val = num
        data = [0]
        while i <= val:
            if (val % i == 0):
                data[0] = i
                val //= i
            i += 1
        return data[-1]

    def copy_all_op() -> None:
        """Simulates Copy All operation"""
        op_count[0] += 1

    def paste_op() -> None:
        """Simulates Paste operation"""
        op_count[0] += 1
        content[0] += 'H'

    if ((not isinstance(n, int)) or (n <= 0) or (n == 1)):
        return 0
    divisor_value = find_div(n)
    division_value = n // divisor_value
    copy_all_op()
    for _ in range(divisor_value - 1):
        paste_op()
    if (len(content[0]) != n):
        copy_all_op()
        for _ in range(division_value - 1):
            paste_op()
    return op_count[-1]
