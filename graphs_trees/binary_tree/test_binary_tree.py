import pytest
from binary_tree import BinaryTree


@pytest.fixture
def empty_tree():
    return BinaryTree()


@pytest.fixture
def non_empty_tree(empty_tree):
    empty_tree.insert(5)
    empty_tree.insert(3)
    empty_tree.insert(7)
    empty_tree.insert(1)
    empty_tree.insert(4)
    empty_tree.insert(6)
    empty_tree.insert(8)
    return empty_tree


def test_pre_order(non_empty_tree):
    assert non_empty_tree.traverse_pre_order() == [5, 3, 1, 4, 7, 6, 8]


def test_in_order(non_empty_tree):
    assert non_empty_tree.traverse_in_order() == [1, 3, 4, 5, 6, 7, 8]


def test_post_order(non_empty_tree):
    assert non_empty_tree.traverse_post_order() == [1, 4, 3, 6, 8, 7, 5]


def test_size(non_empty_tree):
    assert non_empty_tree.size() == 7


def test_height(non_empty_tree):
    assert non_empty_tree.height == 2


def test_find(empty_tree, non_empty_tree):
    assert empty_tree.find(5) is False
    assert non_empty_tree.find(5) is True


def test_insert(empty_tree):
    assert empty_tree.root is None

    empty_tree.insert(5)
    assert empty_tree.root.data == 5
    assert empty_tree.root.left is None
    assert empty_tree.root.right is None
    assert empty_tree.find(5) is True

    empty_tree.insert(3)
    assert empty_tree.root.left is not None
    assert empty_tree.root.left.data == 3

    empty_tree.insert(7)
    assert empty_tree.root.right is not None
    assert empty_tree.root.right.data == 7


def test_remove(non_empty_tree):
    assert non_empty_tree.find(5) is True
    non_empty_tree.remove(5)
    assert non_empty_tree.find(5) is False

    assert non_empty_tree.find(3) is True
    non_empty_tree.remove(3)
    assert non_empty_tree.find(3) is False

    assert non_empty_tree.find(7) is True
    non_empty_tree.remove(7)
    assert non_empty_tree.find(7) is False

    assert non_empty_tree.find(1) is True
    non_empty_tree.remove(1)
    assert non_empty_tree.find(1) is False

    assert non_empty_tree.find(4) is True
    non_empty_tree.remove(4)
    assert non_empty_tree.find(4) is False

    assert non_empty_tree.find(6) is True
    non_empty_tree.remove(6)
    assert non_empty_tree.find(6) is False

    assert non_empty_tree.find(8) is True
    non_empty_tree.remove(8)
    assert non_empty_tree.find(8) is False
    assert non_empty_tree.root is None
