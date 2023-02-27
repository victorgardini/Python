# Problem: Determine if a number is a power of two.

"""
We can use bit manipulation to determine if a number is a power of two.
For a number to be a power of two, there must only be one bit that is a 1.
We can use the following bit manipulation trick to determine this:

>> n & (n - 1)

Here's an example why:
0000 1000 = n
0000 0001 = 1
0000 0111 = n-1

0000 1000 = n
0000 0111 = n-1
0000 0000 = n & n-1, result = 0
"""


def is_power_two(n):
    return n > 0 and not (n & (n - 1))
