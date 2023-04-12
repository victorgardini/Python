from find_second_largest_node import Solution

import pytest


@pytest.mark.parametrize(('nodes', 'expected'), [
    ([], ValueError),
    ([1], ValueError),
    ([5, 3, 7, 2, 4, 6, 8], 7),
    ([5, 3, 7, 2, 4, 6], 6),
    ([5, 3, 7, 2, 4], 5),
    ([5, 3, 7, 2], 5),
    ([5, 3, 7], 5),
    ([5, 3], 3),
])
def test_find_second_largest_node(nodes, expected):
    """ Test find second largest node. """

    binary_tree = Solution()

    for node in nodes:
        binary_tree.insert(node)

    if expected is ValueError:
        with pytest.raises(ValueError):
            binary_tree.find_second_largest_node()
    else:
        assert binary_tree.find_second_largest_node() == expected
        assert binary_tree.find_max() == max(nodes)
