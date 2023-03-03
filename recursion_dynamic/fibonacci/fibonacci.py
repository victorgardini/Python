# Problem: Implement fibonacci recursively, dynamically, and iteratively.

from typing import List


def fibonacci_recursive(n: int) -> int:
    """
    This function returns the nth Fibonacci number recursively.
    :param n: The index of the Fibonacci number to return.
    :return: The nth Fibonacci number.
    """
    if n == 0:  # Base case 1: If n is 0, return 0.
        return 0
    if n == 1:  # Base case 2: If n is 1, return 1.
        return 1

    # Recursive case: The nth Fibonacci number is the sum of the (n - 1)th and (n - 2)th Fibonacci numbers.
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dynamic(n: int) -> int:
    """
    This function returns the nth Fibonacci number dynamically.
    :param n: The index of the Fibonacci number to return.
    :return: The nth Fibonacci number.
    """
    # Initialize the cache to store the Fibonacci numbers.
    cache: List = [None] * (n + 1)

    # Base case 1: If n is 0, return 0.
    cache[0] = 0
    if n == 0:  # prevent index out of range error if n == 0
        return cache[0]

    # Base case 2: If n is 1, return 1.
    cache[1] = 1

    # Dynamic case: The nth Fibonacci number is the sum of the (n - 1)th and (n - 2)th Fibonacci numbers.
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]


def fibonacci_iterative(n: int) -> int:
    """
    This function returns the nth Fibonacci number iteratively.
    :param n: The index of the Fibonacci number to return.
    :return: The nth Fibonacci number.
    """
    # Base case 1: If n is 0, return 0.
    if n == 0:
        return 0

    # Base case 2: If n is 1, return 1.
    if n == 1:
        return 1

    # Initialize the first two Fibonacci numbers.
    a = 0
    b = 1

    # Loop through the Fibonacci numbers until we reach the nth Fibonacci number.
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b
