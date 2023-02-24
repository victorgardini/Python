from radix_sort import radix_sort
import pytest


@pytest.mark.parametrize("array", [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [1, 5, 2, 4, 3],
    [128, 256, 164, 8, 2, 148, 212, 242, 244]
])
def test_radix_sort(array):
    assert radix_sort(array) == sorted(array)
