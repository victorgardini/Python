import pytest
from add_digits import add_digits


@pytest.mark.parametrize("num, expected", [
    (0, 0),  # 0
    (9, 9),  # 9
    (138, 3),  # 1 + 3 + 8 = 12, 1 + 2 = 3
    (38, 2),  # 38 -> 3 + 8 = 11 -> 1 + 1 = 2, so 38 -> 2
    (65536, 7),  # 65536 -> 7 (6 + 5 + 5 + 3 + 6 = 25 -> 2 + 5 = 7)
])
def test_add_digits(num, expected):
    assert add_digits(num) == expected
