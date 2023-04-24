# Problem: swap the values of two variables without using a temporary variable.

def swap_variables(a, b):
    """
    Function implemented to swap the values of two variables without using a temporary variable.
    :param a: first variable.
    :param b: second variable.
    :return: tuple of swapped variables.

    Example:
    >>> swap_variables(1, 2)
    a = 2, b = 1 then
    a = a ^ b = 1 ^ 2 = 3
    b = a ^ b = 3 ^ 2 = 1
    a = a ^ b = 3 ^ 1 = 2

    """
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a, b


def swap_xor(a: int, b: int) -> tuple:
    """
    Function implemented to swap the values of two variables without using a temporary variable.
    :param a: first variable.
    :param b: second variable.
    :return: tuple of swapped variables.

    Example:
    >>> swap_xor(10, 20)
    a = 10, b = 20 then
    a = a ^ b = 10 ^ 20 = 30 (11110)
    b = a ^ b = 30 ^ 20 = 10 (1010)
    a = a ^ b = 30 ^ 10 = 20 (10100)
    """
    a ^= b
    b ^= a
    a ^= b

    return a, b


def swap_add_sub(a: int, b: int) -> tuple:
    """
    Function implemented to swap the values of two variables without using a temporary variable.
    :param a: first variable.
    :param b: second variable.
    :return: tuple of swapped variables.

    Example:
    >>> swap_add_sub(10, 20)
    a = 10, b = 20 then
    a = a + b = 10 + 20 = 30
    b = a - b = 30 - 20 = 10
    a = a - b = 30 - 10 = 20

    """
    a += b
    b = a - b
    a -= b

    return a, b
