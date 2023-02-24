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


def selection_sort_recursive(data: List[int]) -> List[int]:
    """
    Implementation of Selection Sort Algorithm, recursive version.
    :param data: list of numbers.
    :return: list with ordinated data.
    """
    if len(data) == 1:
        return data

    min_index = 0
    for i in range(1, len(data)):  # find min index
        if data[i] < data[min_index]:
            min_index = i
    if data[min_index] < data[0]:  # swap
        data[0], data[min_index] = data[min_index], data[0]

    # Call recursively on the rest of the list
    return [data[0]] + selection_sort_recursive(data[1:])
