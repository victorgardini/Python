import pytest
from flip_bit import flip_bit


@pytest.mark.parametrize(("num", "expected"), [
    (0b00001111110111011110001111110000, 10),
    (0b00000100111011101111100011111011, 9),
    (0b00010011101110111110001111101111, 10),
])
def test_flip_bit(num, expected):
    assert flip_bit(num) == expected
