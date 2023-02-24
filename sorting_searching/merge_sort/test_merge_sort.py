from merge_sort import merge_sort

import pytest


@pytest.mark.parametrize(
    "data", [
        ([1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1]),
        ([1, 5, 2, 4, 3]),
    ]
)
def test_merge_sort(data):
    assert merge_sort(data) == sorted(data)
