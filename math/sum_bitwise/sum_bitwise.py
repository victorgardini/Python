# Problem: Find the sum of two integers without using the + or - sign.

"""
Solution: Use bitwise operators.
Consider the following article https://www.geeksforgeeks.org/bitwise-recursive-addition-two-integers/

Sum of two bits can be obtained by performing XOR (^) of the two bits.
Carry bit can be obtained by performing AND (&) of two bits.
"""


def add(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return add(a ^ b, (a & b) << 1)
