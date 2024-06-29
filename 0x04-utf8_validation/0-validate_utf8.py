#!/usr/bin/python3
"""
UTF8 Validation
"""


def validUTF8(data):
    """
    data: a list of int
    """
    byte_cnt = 0
    for i in data:
        if byte_cnt == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_cnt = 1
            elif i >> 4 == 0b1110:
                byte_cnt = 2
            elif i >> 3 == 0b11110:
                byte_cnt = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_cnt -= 1
        return byte_cnt == 0
