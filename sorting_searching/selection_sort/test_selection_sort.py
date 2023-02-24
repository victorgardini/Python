from selection_sort import selection_sort, selection_sort_recursive

import pytest


@pytest.mark.parametrize(
    "data", [
        ([1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1]),
        ([1, 5, 2, 4, 3]),
    ]
)
def test_selection_sort(data):
    assert selection_sort(data) == sorted(data)
    assert selection_sort_recursive(data) == sorted(data)
