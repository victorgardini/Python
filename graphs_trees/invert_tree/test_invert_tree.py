from invert_tree import InvertTree


def test_invert_tree():
    tree = InvertTree()

    for data in [5, 2, 3, 1, 7, 6, 9]:
        tree.insert(data)

    tree.invert()

    assert tree.traverse_in_order() == [9, 7, 6, 5, 3, 2, 1]
