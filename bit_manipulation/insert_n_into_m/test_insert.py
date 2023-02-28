import pytest
from insert import insert_into


@pytest.mark.parametrize(("n", "m", "i", "j", "expected"), [
    (1201, 8, 3, 6, 1217),
    (0b10000000000, 0b10011, 2, 6, 0b10001001100)
])
def test_insert_into(n, m, i, j, expected):
    assert insert_into(n, m, i, j) == expected
