#!/usr/bin/python3
'''Minimum Operations'''
def minOperations(n):
    """
        function for calculating the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
    """
    p_ch = 1
    clipb = 0
    counter = 0

    while p_ch < n:
        if clipb == 0:
            clipb = p_ch
            counter += 1

        if p_ch == 1:
            p_ch += clipb
            counter += 1
            continue

        remaining = n - p_ch
        if remaining < clipb:
            return 0

        if remaining % p_ch != 0:
            p_ch += clipb
            counter += 1
        else:
            clipb = p_ch
            p_ch += clipb
            counter += 2

    if p_ch == n:
        return counter
    else:
        return 0
