import pytest
from generate_primes import generate_primes


@pytest.mark.parametrize(
    "num, expected",
    [
        (0, []),
        (1, []),
        (2, [2]),
        (3, [2, 3]),
        (4, [2, 3]),
        (5, [2, 3, 5]),
        (6, [2, 3, 5]),
        (7, [2, 3, 5, 7]),
        (8, [2, 3, 5, 7]),
        (9, [2, 3, 5, 7]),
        (10, [2, 3, 5, 7]),
    ],
)
def test_generate_primes(num, expected):
    assert generate_primes(num) == expected
