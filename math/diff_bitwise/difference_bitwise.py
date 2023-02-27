# Problem: Find the difference of two integers without using the + or - sign.

# Solution: Use bitwise operators.


def difference(a: int, b: int) -> int:
    result = (~a & b) << 1  # ~a = -a - 1 = -a - 1 = -(a + 1)
    borrow = a ^ b  # a - b = a + (-b)

    # If bitwise & is 0, then there
    # is not going to be any carry.
    # Hence result of XOR is addition.
    if result == 0:
        return borrow

    return difference(borrow, result)
