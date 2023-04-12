from check_if_binary_tree_is_balanced import Solution

import pytest


@pytest.mark.parametrize('nodes, expected', [
    ([], ValueError),
    ([1], True),
    ([1, 2], True),
    ([1, 2, 3], False),
    ([3, 2, 1, 4, 5], True),
    ([5, 3, 8, 9, 10], False),
    ([3, 2, 1, 5, 4, 6, 7], True),
])
def test_balanced_tree(nodes, expected):
    tree = Solution()

    for value in nodes:
        tree.insert(value)

    if expected is ValueError:
        with pytest.raises(ValueError):
            tree.is_balanced()
    else:
        assert tree.is_balanced() is expected
