# Problem: Implement insertion sort.

from typing import List


def insertion_sort(data: List[int]) -> List[int]:
    """Sort a data using insertion sort."""
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1
    return data
