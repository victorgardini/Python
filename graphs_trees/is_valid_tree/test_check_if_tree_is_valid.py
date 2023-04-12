from check_if_tree_is_valid import Solution


def test_valid_tree():
    tree = Solution()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(5)
    assert tree.is_valid() is True


def test_invalid_tree():
    tree = Solution()

    tree.insert(5)
    tree.insert(3)
    tree.insert(8)
    tree.insert(20)

    # ensure that the tree is invalid
    tree.root.left.data = 100

    assert tree.is_valid() is False
