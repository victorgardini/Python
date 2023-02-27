import pytest
from check_prime import is_prime, is_prime_optimized


@pytest.mark.parametrize("number, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
    (11, True),
    (12, False)
])
def test_check_prime(number, expected):
    assert is_prime(number) == expected
    assert is_prime_optimized(number) == expected
