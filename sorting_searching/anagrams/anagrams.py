# Problem: Sort an array of strings so all anagrams are next to each other.

from collections import OrderedDict
from typing import List


def group_anagrams(words: List[str]) -> List[str]:
    """Group anagrams together in a list of words."""

    # Create a dictionary of anagrams
    anagram_dict = OrderedDict()

    for word in words:
        # Use a tuple, which is hashable and serves as the key in anagram_map
        sorted_chars = tuple(sorted(word))  # ex: ('a', 'm', 'r')
        if sorted_chars in anagram_dict:  # ex: ('a', 'm', 'r') in anagram_map
            anagram_dict[sorted_chars].append(word)  # ex: anagram_map[('a', 'm', 'r')].append('arm')
        else:
            anagram_dict[sorted_chars] = [word]  # ex: anagram_map[('a', 'm', 'r')] = ['arm']

    result = []
    for anagram in anagram_dict.values():  # ex: anagram_map.values() = [['arm'], ['ram'], ['mar']]
        result.extend(anagram)  # ex: result.extend(['arm'])

    return result  # ex: ['arm', 'ram', 'mar']
