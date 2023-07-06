#!/usr/env python3
"""
A functio that unlocks boxes
"""


def canUnlockAll(boxes):
    """
    A function that unlock boxes
    """
    if len(boxes) < 1:
        return False
    # Create a list of keys
    keys = [0]
    # Set of unlocked boxes
    index = 0
    # if we have key
    while index < len(keys):
        if len(boxes[keys[index]]) < 1:
            index += 1
            continue
        for element in boxes[keys[index]]:
            if element not in keys:
                if element < len(boxes):
                    keys.append(element)
        index += 1
    if len(keys) == len(boxes):
        return True
    return False
