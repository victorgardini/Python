# Problem: Find the magic index in an array, where array[i] = i.

from typing import List


def magic_index(array: List[int]) -> int:
    return magic_index_helper(array, 0, len(array) - 1)


def magic_index_helper(array: List[int], start: int, end: int) -> int:
    if end < start or start < 0 or end >= len(array):
        return -1

    mid = (start + end) // 2

    if array[mid] == mid:
        return mid

    # if array[mid] < mid, then we know that the magic index cannot be in the right half.
    left_end = min(mid - 1, array[mid])
    left_result = magic_index_helper(array, start, left_end)  # search left
    if left_result != -1:  # if found the magic index in the left half, then return it.
        return left_result

    # if array[mid] > mid, then we know that the magic index cannot be in the left half.
    right_start = max(mid + 1, array[mid])
    right_result = magic_index_helper(array, right_start, end)  # search right
    if right_result != -1:  # if we found the magic index in the right half, then return it.
        return right_result

    # if we didn't find the magic index in the left half or the right half, then return -1.
    return -1
