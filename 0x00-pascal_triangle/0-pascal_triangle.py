#!/usr/bin/python3
"""
This module houses a definition of a function that generates a
pascal's triangle valuse based on a given value n.
"""


def generate_pascal_elements(m, m_element=[]):
    """
    Generate element for a row m of the pascal triangle

    Args:
        m - the number of a row whose elements are generated
        m_element - list of the element for the row. It is
        initially empty and it is filled and returned

    Returns:
        the list of the element for the given row m
    """

    if (len(m_element) == m):
        return m_element

    if (len(m_element) == 0):
        return generate_pascal_elements(m, [1])

    temp_list = []

    if (len(m_element) < 2 and len(m_element) > 0):
        temp_list.append(1)
        for element in m_element:
            temp_list.append(element)
        return generate_pascal_elements(m, temp_list)

    if (len(m_element) >= 2):
        temp_list.append(1)
        for i in range(len(m_element)):
            current_element = m_element[i]

            try:
                next_element = m_element[i + 1]
            except IndexError:
                next_element = 0

            temp_list.append(current_element + next_element)
        return generate_pascal_elements(m, temp_list)


def pascal_triangle(n):
    """Generates a list of lists that contains a given
    pascal's triangle values

    Args:
        n - the value that determines the pascal's
        triangle value, generated in the lists.

    Returns:
        the list of all rows and their elements for the given size n
    """
    if (n < 1):
        return []

    pascal_elements = []

    row = 0
    while (row < n):
        row_elements = generate_pascal_elements(row + 1)
        pascal_elements.append(row_elements)
        row += 1

    return pascal_elements
