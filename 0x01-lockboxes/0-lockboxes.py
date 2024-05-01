#!/usr/bin/python3
"""Lockboxes challenge"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each inner list represents the keys contained in each box.

    Returns:
        bool: True if all boxes can be opened, else False.

    Example:
        boxes = [[1], [2], [3], [4], []]
        print(canUnlockAll(boxes))  # Output: True
    """
    if not boxes:
        return False
    
    # Initialize a set to keep track of opened boxes
    opened_boxes = {0}
    # Initialize a set to keep track of keys we have
    keys = set(boxes[0])

    # Iterate until there are no new boxes to open
    while True:
        new_boxes = set()
        # Iterate through the keys we currently have
        for key in keys:
            # Check if the key opens a new box
            if key < len(boxes) and key not in opened_boxes:
                new_boxes.update(boxes[key])
                opened_boxes.add(key)
        # If no new boxes were opened in this iteration, break
        if not new_boxes:
            break
        # Update the keys with the new keys we found
        keys.update(new_boxes)

    # If all boxes are opened, return True
    return len(opened_boxes) == len(boxes)
