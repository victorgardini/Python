"""
Challenge: Compress a data such that 'AAABCCDDDDE' becomes 'A3BC2D4E'.
Only compress the data if it saves space.

Solution: Iterate through the data and keep a count of the current character.
If the next character is different than the current character, append the current
and its count to the compressed data. If the compressed data is
longer than the original data, return the original data.

Some things to note:
https://stackoverflow.com/questions/4435169/how-do-i-append-one-string-to-another-in-python/4435752#4435752
"""
from typing import Tuple


class CompressedString:
    def __init__(self, string: str):
        self.string, self._is_compressed = self.compress_string(string)

    @staticmethod
    def compress_string(string: str) -> Tuple[str, bool]:
        """
        Compress a data such that 'AAABCCDDDD' becomes 'A3BC2D4'.
        Only compress the data if it saves space.
        """
        if not string:
            return "", False

        compressed_string = ""
        current_char = string[0]
        count = 0
        for char in string:
            if char == current_char:
                count += 1
            else:
                if count > 1:
                    compressed_string += f"{current_char}{count}"
                else:
                    compressed_string += current_char
                count = 1
                current_char = char

        if count > 1:
            compressed_string += f"{current_char}{count}"
        else:
            compressed_string += current_char

        if len(compressed_string) >= len(string):
            return string, False
        else:
            return compressed_string, True

    @staticmethod
    def uncompress_string(string: str) -> str:
        """
        Uncompress a data such that 'A3BC2D4' becomes 'AAABCCDDDD'.
        """
        uncompressed_string = ""
        count = 0

        for i in range(len(string) - 1, -1, -1):
            if string[i].isdigit():
                count += int(string[i])
            else:
                if count == 0:
                    uncompressed_string += string[i]
                else:
                    uncompressed_string += string[i] * count
                count = 0
        return uncompressed_string[::-1]

    def is_compressed(self) -> bool:
        return self._is_compressed

    def __str__(self) -> str:
        return self.string

    def __repr__(self) -> str:
        return f'CompressedString(data="{self.string}", is_compressed={self._is_compressed})'


if __name__ == "__main__":
    # print(compress_string("AAABCCDDDDE"))
    new_string = CompressedString("AAABCCDDDDE")

    print(new_string.__repr__())
