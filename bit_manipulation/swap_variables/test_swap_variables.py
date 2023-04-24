from bit_manipulation.swap_variables.swap_variables import swap_variables, swap_xor, swap_add_sub
import pytest


@pytest.mark.parametrize("a, b", [
    (1, 2),
    (10, 20),
    (100, 200),
    (1000, 2000),
    (10000, 20000),
])
def test_swap_variables(a, b):
    assert swap_variables(a, b) == (b, a)
