# Problem: Determine the number of bits to flip to convert int a to int b.


def bits_to_flip(a: int, b: int) -> int:
    """
    This function determines the number of bits to flip to convert int a to int b.
    :param a: int
    :param b: int
    :return: int
    """
    count = 0
    while a or b:
        if a & 1 != b & 1:
            count += 1
        a >>= 1
        b >>= 1
    return count


def bits_to_flip_alt(a, b):
    return bin(a ^ b).count('1')
