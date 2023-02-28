import pytest

from bit import Bit


@pytest.fixture
def bit():
    return Bit('10001110')


def test_get_bit(bit):
    assert bit.get_bit(index=3) is True


def test_set_bit(bit):
    expected = int('10011110', base=2)
    assert bit.set_bit(index=4) == expected


def test_clear_bit(bit):
    expected = int('10000110', base=2)
    assert bit.clear_bit(index=3) == expected


def test_clear_bits_msb_to_index(bit):
    expected = int('00000110', base=2)
    assert bit.clear_bits_msb_to_index(index=3) == expected


def test_clear_bits_index_to_lsb(bit):
    expected = int('10000000', base=2)
    assert bit.clear_bits_index_to_lsb(index=3) == expected


def test_update_bit(bit):
    expected = int('10000110', base=2)
    assert bit.update_bit(index=3, value=0) == expected
