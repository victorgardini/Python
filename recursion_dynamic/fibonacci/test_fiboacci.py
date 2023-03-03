from fibonacci import fibonacci_recursive, fibonacci_dynamic, fibonacci_iterative
import pytest


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (11, 89),
    (12, 144),
    (13, 233),
])
def test_fibonacci(n, expected):
    assert fibonacci_recursive(n) == expected
    assert fibonacci_dynamic(n) == expected
    assert fibonacci_iterative(n) == expected
