# Problem: Check if a number is prime.


"""
For a number to be prime, it must be 2 or greater and cannot be divisible by another number other than itself (and 1).

Solution 1 and 2 base:
- We'll check by dividing all numbers from 2 to the input number to determine if the number is prime.

Tip:
As an optimization, we can divide from 2 to the square root of the input number. For each value
that divides the input number evenly, there is a complement b where a * b = n.
If a > sqrt(n) then b < sqrt(n) because sqrt(n^2) = n.

- Consider the following explanation about it: https://www.geeksforgeeks.org/prime-numbers/

"""

from math import sqrt


def is_prime(num: int) -> bool:
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def is_prime_optimized(num: int) -> bool:
    if num < 2:
        return False

    # You don't have to divide by every number.
    # You only have to divide by each prime number between 2 and the square root of your number.
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True
