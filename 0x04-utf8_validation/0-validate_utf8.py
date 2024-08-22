#!/usr/bin/python3
"""
This module houses the definiton of a function, named validUTF8
"""
from typing import List, Union


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
    if (not isinstance(data, list)) and (not isinstance(data, int)):
        return
    is_valid: bool
    if isinstance(data, list):
        for num in data:
            is_valid = bytes([num]).isascii()
            if not is_valid:
                return False
        return True
    if isinstance(data, int):
        is_valid = bytes([data]).isascii()
        if not is_valid:
            return False
    return True
