from binary_search import binary_search
import pytest


@pytest.mark.parametrize(
    "array, value, expected",
    [
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 2, 1),
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 4, 3),
    ],
)
def test_binary_search(array, value, expected):
    assert binary_search(array, value) == expected

