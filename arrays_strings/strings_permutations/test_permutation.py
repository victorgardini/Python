import pytest

from permutation import is_permutation, is_permutation_alt


@pytest.mark.parametrize("string1, string2, expected", [
    ("", "", False),
    (None, "", False),
    ("abc", None, False),
    ("Nib", "bin", False),
    ("act", "cat", True),
    ("a ct", "ca t", True)
])
def test_is_permutation(string1, string2, expected):
    assert is_permutation(string1, string2) is expected
    assert is_permutation_alt(string1, string2) is expected
