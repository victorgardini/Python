from search_sorted_matrix import search_sorted_matrix
import pytest


@pytest.mark.parametrize("matrix, item, expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, (0, 0)),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, (1, 1)),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9, (2, 2)),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, None),
])
def test_search_sorted_matrix(matrix, item, expected):
    assert search_sorted_matrix(matrix, item) == expected
