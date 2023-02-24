# Problem: Implement binary search
from typing import List, Optional


def binary_search(array: List[int], value: int) -> Optional[int]:
    """
    Search for a value in a sorted array using binary search.
    :param array: The array to search in.
    :param value: The value to search for.
    :return: The index of the value in the array, or None if the value is not in the array.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if array[middle] == value:
            return middle
        elif array[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

    return None
