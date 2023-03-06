# Problem: Find all permutations of an input string.

from typing import List


def max_permutations(string: str) -> List[str]:
    if len(string) == 0:  # if string is empty cannot return any permutations
        return [""]

    perms = []  # initialize list to store permutations

    for i in range(len(string)):  # iterate through string
        before = string[:i]  # get all characters before current character
        after = string[i+1:]  # get all characters after current character
        partial_perms = max_permutations(before + after)  # get all permutations of remaining characters

        # iterate through all permutations of remaining characters
        for partial_perm in partial_perms:
            if string[i] + partial_perm not in perms:  # if permutation not already in list, add it
                perms.append(string[i] + partial_perm)

    return perms
