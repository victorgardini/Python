from anagrams import group_anagrams

import pytest


@pytest.mark.parametrize(
    "words, expected", [
        (['ram', 'act', 'arm', 'bat', 'cat', 'tab'], ['ram', 'arm', 'act', 'cat', 'bat', 'tab']),
    ]
)
def test_group_anagrams(words, expected):
    assert group_anagrams(words) == expected
