#!/usr/bin/python3
"""
Locked Boxes
"""


def canUnlockAll(boxes):
    """
    Unlock Boxes
    """
    if not boxes:
        return False

    unlocked = set()
    unlocked.add(0)
    keys = list(boxes[0])
    while keys:
        key = keys.pop()
        if key not in unlocked and key < len(boxes):
            unlocked.add(key)
            keys.extend(boxes[key])
    return len(unlocked) == len(boxes)
