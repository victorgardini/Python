# Problem: Flip one bit from 0 to 1 to maximize the longest sequence of 1s.


def flip_bit(num):
    """
    Function implemented to flip one bit from 0 to 1 to maximize the longest sequence of 1s.ß
    :param num: number to be flipped.
    :return: number of 1s after flipping one bit.
    """
    if ~num == 0:  # if all bits are 1s
        return 8 * 4  # 32 bits

    # initialize control variables
    current_length = 0
    previous_length = 0
    max_length = 1

    while num != 0:  # while there are still bits to be processed
        if (num & 1) == 1:  # if the current bit is 1
            current_length += 1  # increment the current length
        elif (num & 1) == 0:  # if the current bit is 0
            previous_length = 0 if (num & 2) == 0 else current_length  # update the previous length
            current_length = 0  # reset the current length
        max_length = max(previous_length + current_length + 1, max_length)  # update the max length
        num >>= 1  # shift the number to the right

    return max_length
