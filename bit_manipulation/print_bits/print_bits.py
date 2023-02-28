# Problem: Given a real number between 0 and 1, print the binary representation.
# If the length of the representation is > 32, return 'ERROR'.

_MAX_BITS_LENGTH = 32


def printb(num: int):
    if num is None or num >= 1 or num <= 0:     # invalid options
        return 'ERROR'

    binary = ['0', '.']  # start binary representation with '0.'

    while num > 0:  # while we have a number to convert
        if len(binary) >= _MAX_BITS_LENGTH:  # if we have more than 32 bits return error string
            return 'ERROR'

        result = num * 2  # Multiply by 2 to shift the binary point
        if result >= 1:  # if the result is greater than 1, we have a 1 in the binary representation.
            binary.append('1')
            num = result - 1  # subtract 1 from the result to get the remainder
        else:  # if the result is less than 1, we have a 0 in the binary representation.
            binary.append('0')
            num = result  # the remainder is the result

    # return the binary representation as a string using the join method.
    return ''.join(binary)
