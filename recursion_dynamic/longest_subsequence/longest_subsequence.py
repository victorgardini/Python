# Problem: Given two strings, find the longest common subsequence.


def search_longest_common_subsequence(str0: str, str1: str) -> str:
    """
    Given two strings text1 and text2, return the length of their longest common subsequence.
    If there is no common subsequence, return 0.

    Consider read these documentation:
    - https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    - https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
    """
    num_rows = len(str0) + 1
    num_cols = len(str1) + 1

    # Create a 2D array with zeros
    dp = [[0] * num_cols for _ in range(num_rows)]

    for row in range(1, num_rows):
        for col in range(1, num_cols):
            if row == 0 or col == 0:  # First row and first column are zeros by default
                dp[row][col] = 0
            elif str0[row - 1] == str1[col - 1]:  # If the last characters are the same then add 1 to the diagonal.
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:  # If the last characters are different then take the maximum of the top and left cells.
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    # Backtrack to find the longest common subsequence
    result = []
    i = num_rows - 1
    j = num_cols - 1
    while i > 0 and j > 0:  # Start from the bottom right corner and one by one store characters in result[].
        # If current character in X[] and Y are same, then current character is part of LCS.
        # Then move diagonally up to left.
        if str0[i - 1] == str1[j - 1]:
            result.append(str0[i - 1])
            i -= 1
            j -= 1

        # If not same, then find the larger of two and go in the direction of larger value.
        # Then move vertically up in the table.
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        # Else move horizontally left in the table.
        else:
            j -= 1

    # Since we traverse the DP table from bottom right to top left, we need to reverse the result.
    return ''.join(result[::-1])
