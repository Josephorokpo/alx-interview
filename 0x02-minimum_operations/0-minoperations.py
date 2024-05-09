#!/usr/bin/python3
'''Minimum Operations python3 challenge'''

def minOperations(n):
    '''
    Calculates the fewest number of operations needed to result in exactly n H
    characters in this file.
    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required, or 0 if impossible.
    '''
    pasted_chars = 1  # Number of characters in the file
    clipboard = 0  # Number of 'H's copied
    counter = 0  # Operations counter

    while pasted_chars < n:
        # If nothing has been copied yet
        if clipboard == 0:
            # Copy all
            clipboard = pasted_chars
            # Increment operations counter
            counter += 1

        # If nothing has been pasted yet
        if pasted_chars == 1:
            # Paste
            pasted_chars += clipboard
            # Increment operations counter
            counter += 1
            # Continue to next loop iteration
            continue

        remaining = n - pasted_chars  # Remaining chars to paste
        # Check if impossible by comparing clipboard size
        # with the remaining characters needed
        if remaining < clipboard:
            return 0

        # If it can't be divided evenly
        if remaining % pasted_chars != 0:
            # Paste current clipboard
            pasted_chars += clipboard
            # Increment operations counter
            counter += 1
        else:
            # Copy all
            clipboard = pasted_chars
            # Paste
            pasted_chars += clipboard
            # Increment operations counter
            counter += 2

    # If the desired result is achieved
    if pasted_chars == n:
        return counter
    else:
        return 0
