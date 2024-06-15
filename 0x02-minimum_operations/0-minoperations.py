#!/usr/bin/python3
"""
Module Docs
"""


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed to result in exactly
    n 'H' characters in the file.

    Args:
    - n (int): The desired number of 'H' characters.

    Returns:
    - int: The fewest number of operations needed. If n is impossible to
    achieve, return 0.
    """
    if not isinstance(n, int) or n <= 0:
        return 0

    operations = 0
    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    # If n is a prime number greater than 1, add it to operations
    if n > 1:
        operations += n

    return operations
