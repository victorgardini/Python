from merge_sorted_arrays import merge_sorted_arrays
import pytest


@pytest.mark.parametrize(
    "array1, array2",
    [
        ([1, 3, 5, 7], [2, 4, 6, 8]),
        ([1, 3, 5, 7], [2, 4, 6, 8, 10]),
        ([1, 3, 5, 7, 9], [2, 4, 6, 8]),
        ([1, 2, 3], [4, 5, 6]),
    ],
)
def test_merge_sorted_arrays(array1, array2):
    assert merge_sorted_arrays(array1, array2) == sorted(array1 + array2)
