import pytest
from ops_solution import Solution


def test_math_ops():
    solution = Solution()

    with pytest.raises(TypeError):
        solution.insert(None)

    solution.insert(5)
    solution.insert(2)
    solution.insert(7)
    solution.insert(9)
    solution.insert(9)
    solution.insert(2)
    solution.insert(9)
    solution.insert(4)
    solution.insert(3)
    solution.insert(3)
    solution.insert(2)

    assert solution.max == 9
    assert solution.min == 2
    assert solution.mean == 5
    assert solution.mode in (2, 9)
