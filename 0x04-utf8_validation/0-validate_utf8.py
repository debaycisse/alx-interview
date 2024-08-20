#!/usr/bin/python3
"""
This module houses the definiton of a function, named validUTF8
"""
from typing import List, Union


def convert_to_base_two(num: int) -> str:
    """
    Converts a given number to its binary form

    Args:
        num - the number whose binary is to be obtained

    Returns:
        the binary representation of the given number
    """
    a: int = num
    b: List[int] = []
    c: str = '0'
    while a > 1:
        b.insert(0, a % 2)
        a //= 2
    for num in b:
        c += '{0}'.format(num)
    return c


def is_int_list(data: List[int]) -> bool:
    """
    Confirms that a given data variable is a list of integers

    Args:
        data - the variable to be validated

    Returns:
        True, if a given variable is a list of integers, otherwise false
    """
    for num in data:
        if not isinstance(num, int):
            return False
    return True


def validUTF8(data: Union[List[int], int]) -> bool:
    """
    Confirms that a given data (integer) is a valid UTF8
    character set, found in its 1 byte code point

    Args:
        data - the data, which may be a number or
        list of number to be validated

    Returns:
        True, if it is a valid UTF8 character set, otherwise false
    """
    if (not isinstance(data, int)) and (not is_int_list(data)):
        raise ValueError('data must be integer or list of integer')

    if isinstance(data, list):
        for num in data:
            res: str = convert_to_base_two(num)
            if len(res) > 8:
                return False
        return True

    res = convert_to_base_two(data)
    if len(res) > 8:
        return False
    return True
