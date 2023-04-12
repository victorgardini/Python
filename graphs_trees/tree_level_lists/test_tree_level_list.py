from tree_level_lists import TreeLevelLists


def test_tree_level_list():
    tree = TreeLevelLists()

    for data in [5, 3, 8, 2, 4, 1, 7, 6, 9, 10, 11]:
        tree.insert(data)

    assert tree.create_level_lists() == [[5], [3, 8], [2, 4, 7, 9], [1, 6, 10], [11]]
