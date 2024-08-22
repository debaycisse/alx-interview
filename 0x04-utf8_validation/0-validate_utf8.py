#!/usr/bin/python3
"""
This module houses the definiton of a function, named validUTF8
"""


def validUTF8(data):
    """
    Confirms that a given data (integer) is a valid UTF8
    character set, found in its 1 byte code point

    Args:
        data - the data, which may be a number or
        list of number to be validated

    Returns:
        True, if it is a valid UTF8 character set, otherwise false
    """
    if not isinstance(data, list):
        return False
    try:
        converted_data = bytes([num & 255 for num in data])
        converted_data.decode('UTF-8')
        return True
    except UnicodeDecodeError:
        return False
