# Problem: Determine the total number of unique ways to make n cents, given coins of denominations less than n cents.

from typing import List


def coin_change(n: int, coins : List[int]) -> int:
    """
    This function returns the total number of unique ways to make n cents,
    given coins of denominations less than n cents.
    :param n: The amount of cents to make.
    :param coins: The denominations of coins to use.
    :return: The total number of unique ways to make n cents.
    """
    if n == 0:  # Base case 1: If n is 0, there is 1 way to make 0 cents.
        return 1
    if n < 0:  # Base case 2: If n is less than 0, there is 0 ways to make n cents.
        return 0
    if len(coins) == 0:  # Base case 3: If there are no coins, there is 0 ways to make n cents.
        return 0

    # Recursive case: The total number of ways to make n cents is the sum of the number of
    # ways to make n - coins[0] cents and the number of ways to make n cents with coins[1:].
    return coin_change(n - coins[0], coins) + coin_change(n, coins[1:])
