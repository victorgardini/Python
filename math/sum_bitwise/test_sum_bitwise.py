import pytest
from sum_bitwise import add


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1),
        (2, 2)
    ]
)
def test_add(a, b):
    assert add(a, b) == a + b
