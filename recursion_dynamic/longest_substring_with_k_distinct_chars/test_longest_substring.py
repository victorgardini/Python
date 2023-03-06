from longest_substring import longest_substring
import pytest


@pytest.mark.parametrize(("s", "k", "expected"), [
    ("abcba", 2, 3),
    ('abcabcdefgghiij', 3, 6),
    ('abcabcdefgghighij', 3, 7),
])
def test_longest_substring(s, k, expected):
    assert longest_substring(s, k) == expected
