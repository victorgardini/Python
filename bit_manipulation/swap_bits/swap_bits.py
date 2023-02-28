# Problem: Swap the odd and even bits of a positive integer with as few operations as possible.

def swap_bits(num):
    """
    Function implemented to swap the odd and even bits of a positive integer with as few operations as possible.
    :param num: number to be swapped.
    :return: number with odd and even bits swapped.
    """
    odd = (num & 0b1010101010101010) >> 1  # get the odd bits
    even = (num & 0b0101010101010101) << 1  # get the even bits

    return odd | even  # combine the odd and even bits
