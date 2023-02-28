import pytest

from print_bits import printb


@pytest.mark.parametrize('num, expected', [
    (0.5, '0.1'),
    (0.25, '0.01'),
    (0.75, '0.11'),
    (0.125, '0.001'),
    (0, 'ERROR'),
    (1, 'ERROR'),
    (None, 'ERROR'),
])
def test_printb(num, expected):
    assert printb(num) == expected
