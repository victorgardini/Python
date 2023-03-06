from longest_subsequence import search_longest_common_subsequence
import pytest


@pytest.mark.parametrize(("str1", "str2", "expected"), [
    ('ABCDEFGHIJ', 'FOOBCDBCDE', 'BCDE'),
    ('ABCDGH', 'AEDFHR', 'ADH'),
    ('AGGTAB', 'GXTXAYB', 'GTAB'),
])
def test_longest_common_subsequence(str1, str2, expected):
    assert search_longest_common_subsequence(str1, str2) == expected
