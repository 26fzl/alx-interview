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

    db = 1
    beg = 0
    counter = 0
    while db < n:
        remainder = n - db
        if (remainder % db == 0):
            beg = db
            db += beg
            counter += 2
        else:
            db += beg
            counter += 1
    return counter
