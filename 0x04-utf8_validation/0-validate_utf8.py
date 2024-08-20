#!/usr/bin/python3
"""
#TODO:
"""


def convert_to_base_two(num: int) -> str:
    """
    #TODO:
    """
    a = num
    b = []
    c = '0'
    while a > 1:
        b.insert(0, a % 2)
        a //= 2
    
    for num in b:
        c += num

    return c

def validUTF8(data: Union[List[int], int]) -> bool:
    """
    #TODO:
    """
    if isinstance(data, list):
        #TODO:  Do the below in an iteration
        # call convert_to_base_two function to obtain the binary of a number
        # check if the length is greater than 8 bits
            # YES:  return FALSE
            # NO:  return TRUE
            
    else:
        # call convert_to_base_two function to obtain the binary of a number
        # check if the length is greater than 8 bits
            # YES:  return FALSE
            # NO:  return TRUE
