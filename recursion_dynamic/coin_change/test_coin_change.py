from coin_change import coin_change
import pytest


@pytest.mark.parametrize("n, coins, expected", [
    (0, [1, 2, 3], 1),
    (1, [1, 2, 3], 1),
    (2, [1, 2, 3], 2),
    (3, [1, 2, 3], 3),
    (4, [1, 2, 3], 4),
])
def test_coin_change(n, coins, expected):
    assert coin_change(n, coins) == expected
