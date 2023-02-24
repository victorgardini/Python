# Problem: Implement radix sort.

from typing import List


def radix_sort(array: List[int]) -> List[int]:

    max_value = max(array)  # Find the maximum value in the array
    max_digit = len(str(abs(max_value)))  # Find the number of digits in the max value ex. 1000 = 4 digits
    current_array = array  # Set the current array to the original array

    for digit in range(max_digit):  # Loop through each digit
        buckets = [[] for _ in range(10)]  # Create 10 buckets for each digit
        for number in current_array:  # Loop through each number in the current array
            digit_value = (number // 10 ** digit) % 10  # Get the digit value
            buckets[digit_value].append(number)  # Append the number to the bucket
        current_array = [number for bucket in buckets for number in bucket]  # Flatten the buckets

    return current_array  # Return the sorted array
