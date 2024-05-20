#!/usr/bin/python3
"""
Module to determine if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers where each integer represents
        a byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0
    for num in data:
        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if num >> 7 == 0:  # 1-byte character
                continue
            elif num >> 5 == 0b110:  # 2-byte character
                n_bytes = 1
            elif num >> 4 == 0b1110:  # 3-byte character
                n_bytes = 2
            elif num >> 3 == 0b11110:  # 4-byte character
                n_bytes = 3
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if num >> 6 != 0b10:
                return False
        n_bytes -= 1
    return n_bytes == 0
