# Problem: Generate a list of primes.

# Solution: Use the Sieve of Eratosthenes.
# Consider reading: https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/

from typing import List


def generate_primes(num: int) -> List[int]:
    primes = []
    is_prime = [False, False] + [True] * (num - 1)
    for p in range(2, num + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, num + 1, p):
                is_prime[i] = False
    return primes
