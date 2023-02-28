import pytest
from swap_bits import swap_bits


@pytest.mark.parametrize(("num", "expected"), [
    (0b0000100111110110, 0b0000011011111001),
])
def test_swap_bits(num, expected):
    assert swap_bits(num) == expected
