# Problem: Given sorted arrays A, B, merge B into A in sorted order.

from typing import List


def merge_sorted_arrays(array1: List[int], array2: List[int]) -> List[int]:
    """
    >>> merge_sorted_arrays([1, 3, 5, 7], [2, 4, 6, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    :param array1: sorted array.
    :param array2: sorted array.
    :return: sorted array.
    """
    array1_index = 0
    array2_index = 0
    merged_array = []

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            merged_array.append(array1[array1_index])
            array1_index += 1
        else:
            merged_array.append(array2[array2_index])
            array2_index += 1

    while array1_index < len(array1):
        merged_array.append(array1[array1_index])
        array1_index += 1

    while array2_index < len(array2):
        merged_array.append(array2[array2_index])
        array2_index += 1

    return merged_array
