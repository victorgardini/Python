# Problem: Given two 16 bit numbers, n and m, and two indices i, j, insert m into n such
# that m starts at bit j and ends at bit i.
#
# Example:
# Input: n = 10000000000, m = 10011, i = 2, j = 6
# Output: n = 10001001100


def insert_into(n, m, i, j):
    """
    This function inserts m into n such that m starts at bit j and ends at bit i. The
    function returns the result of the insertion.
    :param n: number to be inserted into.
    :param m: number to be inserted.
    :param i: starting index.
    :param j: ending index.
    :return: n with m inserted.
    """

    clear_mask = -1 << (j + 1)
    capture_mask = (1 << i) - 1

    # Capturing bits from i-1 to 0
    captured_bits = n & capture_mask

    # Clearing bits from j to 0
    n &= clear_mask

    # Shifting m to align with n
    m = m << i

    # Insert m into n
    n |= m

    # Insert captured bits
    n |= captured_bits

    return n
