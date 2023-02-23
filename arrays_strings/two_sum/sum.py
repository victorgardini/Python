from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Returns the indices of the two numbers that sum to target. If no such numbers exist, returns an empty list.
    :param numbers: A list of integers.
    :param target: The target sum.
    :return: The indices of the two numbers that sum to target.
    """
    # Create a dictionary to store the difference between the target and the
    # current number as the key and the index as the value.
    diff_dict = {}  # ex. {7: 0, 2: 1, -2: 2, -6: 3}

    for index, num in enumerate(numbers):
        # If the current number is in the dictionary, return the index of the current number and the
        # value of the current number in the dictionary.
        if num in diff_dict:
            return [diff_dict[num], index]
        # Otherwise, we store the difference between the target and the current
        # number as the key and the index as the value.
        else:
            diff_dict[target - num] = index

    # If no two numbers sum to target, return an empty List.
    return []

