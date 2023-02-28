import pytest
from bits_to_flip import bits_to_flip, bits_to_flip_alt


@pytest.mark.parametrize(("a", "b", "expected"), [
    (0b11101, 0b01111, 2),
    (0b11101, 0b11111, 1),
])
def test_bits_to_flip(a, b, expected):
    assert bits_to_flip(a, b) == expected
    assert bits_to_flip_alt(a, b) == expected
