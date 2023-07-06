#!/usr/env python3


def canUnlockAll(boxes):
    if len(boxes) < 1:
        return False
    keys = [0]
    index = 0
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
