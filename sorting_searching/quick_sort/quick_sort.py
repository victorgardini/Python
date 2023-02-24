# Problem: Implement quick sort.

from typing import List


def quick_sort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array

    left = []
    equal = []
    right = []
    pivot_index = len(array) // 2
    pivot = array[pivot_index]

    # Split the array into two parts (left and right)
    for i in array:
        if i == pivot:
            equal.append(i)
        elif i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)

    return quick_sort(left) + equal + quick_sort(right)
