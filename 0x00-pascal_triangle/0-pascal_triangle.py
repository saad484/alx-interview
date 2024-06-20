#!/usr/bin/env python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    pascal triangle O(n^2)
    """

    if n <= 0:
        return res[[]]

    res = [[1]]
    for i in range(n-1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
