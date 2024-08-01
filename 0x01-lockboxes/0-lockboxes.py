#!/usr/bin/python3
"""This modules contains the definition of a function, named canUnlockAll"""


def contain_key(boxes, idx):
    """
    determines if an opened box contains a key to the next box

    Args:
        boxes - a list of locked boxes (lists)
        idx - index of an opened box to be checked

    Returns:
        True, if at least one key is found, otherwise False
    """
    if (len(boxes[idx]) >= 1):
        return True
    return False


def next_boxes(boxes, idx):
    """
    determines if next locked box exist in the boxes or not

    Args:
        boxes - a list of locked boxes (lists)
        idx - index of the current opened box

    Returns:
        True, if the current box is not the last locked box, otherwise False
    """
    try:
        if (boxes[idx + 1]):
            return True
        elif (len(boxes[idx + 1]) == 0):
            return True
    except Exception:
        return False


def canUnlockAll(boxes, idx=0, proceed=True, outcome=None):
    """
    iterates through all locked boxes (lists, caontained in a list)
    and determines if all the locked boxes can be opened or not

    Args:
        boxes - holds the list of the lists that contain
        the keys to open the next locked box

        idx - the index value of the current box to be checked

        proceed - indicates if the recursion should take place or not

        outcome - indicates the conclusion after visiting all locked
        boxes or encountering no key for a next locked box or boxes

    Returns:
        True, if all locked boxes can be opened, otherwise, False
    """
    if (proceed is True and outcome is None):
        if (contain_key(boxes, idx)):
            if (next_boxes(boxes, idx)):
                return canUnlockAll(boxes, idx=idx + 1,
                                    proceed=True, outcome=None)
            else:
                return canUnlockAll(boxes, idx=idx,
                                    proceed=False, outcome=True)
        else:
            if (not next_boxes(boxes, idx)):
                return canUnlockAll(boxes, idx=idx,
                                    proceed=False, outcome=True)
            else:
                return canUnlockAll(boxes, idx=idx,
                                    proceed=False, outcome=False)

    if (outcome is True):
        return True
    return False
