# Problem: Implement selection sort.

from typing import List


def selection_sort(data: List[int]) -> List[int]:
    """
    Implementation of Selection Sort Algorithm.
    :param data: list of numbers.
    :return: list with ordinated data.
    """
    for i in range(len(data) - 1):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        if data[min_index] < data[i]:  #
            data[i], data[min_index] = data[min_index], data[i]
    return data
