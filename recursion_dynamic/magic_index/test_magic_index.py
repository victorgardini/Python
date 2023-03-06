from magic_index import magic_index
import pytest


@pytest.mark.parametrize(("array", "expected"), [
    ([-4, -2, 2, 6, 6, 6, 6, 10], 2),
    ([-4, -2, 1, 6, 6, 6, 6, 10], 6),
    ([-4, -2, 1, 6, 6, 6, 7, 10], -1)
])
def test_magic_index(array, expected):
    assert magic_index(array) == expected
