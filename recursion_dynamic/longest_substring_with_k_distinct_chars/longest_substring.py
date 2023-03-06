# Problem: Find the length longest substring with at most k distinct characters.

# Solution: We can use a sliding window to solve this problem. We can use a set to keep
# track of the distinct characters in the current window. If the set size is less than
# or equal to k, we can expand the window to the right. If the set size is greater
# than k, we can shrink the window from the left. We can keep track of the maximum
# length of the window that satisfies the condition.

def longest_substring(string: str, distinct_characters: int) -> int:
    """
    This function returns the length of the longest substring with at most distinct_characters distinct characters.
    :param string: The string to search.
    :param distinct_characters: The maximum number of distinct characters.
    :return: The length of the longest substring with at most distinct_characters distinct characters.
    """
    if not string or distinct_characters == 0:
        return 0

    # If the string is shorter than the number of distinct characters, return the length of the string.
    if len(string) <= distinct_characters:
        return len(string)

    # The left and right pointers of the sliding window.
    max_len = 0  # The maximum length of the substring.
    for i in range(len(string)):  # The left pointer.
        for j in range(i, len(string)):  # The right pointer.
            if len(set(string[i:j + 1])) <= distinct_characters:  # If the set size is less than or equal to k.
                max_len = max(max_len, j-i+1)  # Update the maximum length.

    # Return the maximum length.
    return max_len
