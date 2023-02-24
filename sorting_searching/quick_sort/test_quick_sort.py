from quick_sort import quick_sort
import pytest


@pytest.mark.parametrize(
    "data", [
        ([1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1]),
        ([1, 5, 2, 4, 3]),
    ]
)
def test_insertion_sort(data):
    assert quick_sort(data) == sorted(data)
