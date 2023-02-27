# Problem: Find the sum of two integers without using the + or - sign.

"""
Solution: Use bitwise operators.
Consider the following article https://www.geeksforgeeks.org/bitwise-recursive-addition-two-integers/

Sum of two bits can be obtained by performing XOR (^) of the two bits.
Carry bit can be obtained by performing AND (&) of two bits.
"""


def add(a: int, b: int) -> int:
    keep = (a & b) << 1
    res = a ^ b

    # If bitwise & is 0, then there
    # is not going to be any carry.
    # Hence result of XOR is addition.
    if keep == 0:
        return res

    return add(keep, res)
