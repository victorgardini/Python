import pytest

from sum import two_sum


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([3, 2, 3], 6, [0, 2]),
        ([3, 2, 4], 125, []),
    ],
)
def test_two_sum(numbers, target, expected):
    assert two_sum(numbers, target) == expected
