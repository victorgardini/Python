# Problem: Implement common bit manipulation operations:
# get_bit, set_bit, clear_bit, clear_bits_msb_to_index, clear_bits_msb_to_lsb, update_bit.


class Bit:
    def __init__(self, num: str):
        self.num = int(num, base=2)

    def get_bit(self, index):
        """
        This is a bit tricky. We need to shift the number to the right by index
        and then AND it with 1. This will give us the value of the bit at the
        index.
        :param index: index of the bit. 0 is the least significant bit. 7 is the most significant bit.
        :return: value of the bit at the index.
        """
        return (self.num & (1 << index)) != 0

    def set_bit(self, index):
        """
        This is a bit tricky. We need to shift the number to the right by index
        and then OR it with 1. This will give us the value of the bit at the
        index.
        :param index: index of the bit. 0 is the least significant bit. 7 is the most significant bit.
        :return: value of the bit at the index.
        """
        return self.num | (1 << index)

    def clear_bit(self, index):
        """
        This is a bit tricky. We need to shift the number to the right by index
        and then AND it with 0. This will give us the value of the bit at the
        index.
        :param index: index of the bit. 0 is the least significant bit. 7 is the most significant bit.
        :return: value of the bit at the index.
        """
        return self.num & ~(1 << index)

    def clear_bits_msb_to_index(self, index):
        """
        This is a bit tricky. We need to shift the number to the right by index
        and then AND it with 0. This will give us the value of the bit at the
        index.
        :param index: index of the bit. 0 is the least significant bit. 7 is the most significant bit.
        :return: value of the bit at the index.
        """
        return self.num & ((1 << index) - 1)

    def update_bit(self, index, value):
        """
        This is a bit tricky. We need to shift the number to the right by index
        and then AND it with 0. This will give us the value of the bit at the
        index.
        :param index: index of the bit. 0 is the least significant bit. 7 is the most significant bit.
        :param value: value to update the bit at the index.
        :return: value of the bit at the index.
        """
        return self.num & ~(1 << index) | (value << index)
