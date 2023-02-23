from collections import Counter, defaultdict


def is_permutation(string1, string2):
    if not string1 or not string2:
        return False

    if len(string1) != len(string2):
        return False
    return Counter(string1) == Counter(string2)


def is_permutation_alt(string1, string2) -> bool:
    if not string1 or not string2:
        return False
    if len(string1) != len(string2):
        return False

    char_str1_count = defaultdict(int)
    char_str2_count = defaultdict(int)
    for char in string1:
        char_str1_count[char] += 1
    for char in string2:
        char_str2_count[char] += 1

    return char_str1_count == char_str2_count
