#!/usr/bin/python3

"""Function calculate the MinimumOperations """


def minOperations(n):
    """
    Calculate the minimum numbers of operations needed to result
    in exactly n 'H' charachters in the file

    Args:
    - n (int): The desired number of 'H' charachters.

    Returns:
    - int: The minimum number of operations needed if n
        is impossible to achieve,
    return 0.
    """

    if not isinstance(n, int) or n <= 0:
        return 0

    operations = 0
    divisor = 2

    while divisor * divisor <= 2:
        if n % divisor == 0:
            n //= divisor
            operations += n
        else:
            divisor += 1
    '''if n is prime number greater than 1, add it to operations'''
    if n > 1:
        operations += n

    return operations
