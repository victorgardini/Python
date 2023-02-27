import pytest
from difference_bitwise import difference


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (0, 0),
        (1, 0),
        (10, 1),
        (87, 2)
    ]
)
def test_difference(a, b):
    assert difference(a, b) == a - b
