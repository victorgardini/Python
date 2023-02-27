import pytest
from is_power_of_two import is_power_two


@pytest.mark.parametrize("n, expected", [
    (0, False),
    (1, True),
    (2, True),
    (3, False),
    (4, True),
    (5, False),
    (6, False),
    (7, False),
    (8, True),
    (9, False),
    (10, False),
])
def test_is_power_of_two(n, expected):
    assert is_power_two(n) == expected
