import pytest

from src import LinkedList


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def non_empty_ordered_list():
    non_empty_list = LinkedList()
    for i in range(1, 4):
        non_empty_list.append(data=i)
    return non_empty_list


def test_initialize_list_empty(empty_list):
    assert empty_list.head is None
    assert len(empty_list) == 0


def test_insert_new_node_into_head(empty_list):
    empty_list.append_head(1)
    assert empty_list.head.data == 1
    assert len(empty_list) == 1
    assert empty_list.head.next is None

    empty_list.append_head(2)
    assert empty_list.head.data == 2
    assert len(empty_list) == 2
    assert empty_list.head.next is not None
    assert empty_list.head.next.data == 1

    empty_list.append_head(3)
    assert empty_list.head.data == 3
    assert len(empty_list) == 3
    assert empty_list.head.next is not None
    assert empty_list.head.next.data == 2


def test_insert_new_node_into_tail(empty_list):
    empty_list.append(1)
    assert empty_list.head.next is None
    assert empty_list.head.data == 1
    assert len(empty_list) == 1

    empty_list.append(2)
    assert empty_list.head.next is not None
    assert empty_list.head.next.data == 2
    assert len(empty_list) == 2

    empty_list.append(3)
    assert empty_list.head.next is not None
    assert empty_list.head.next.data == 2
    assert len(empty_list) == 3


def test_find_empty_list_nodes(empty_list):
    assert empty_list.find(1) is None
    assert empty_list.find(2) is None
    assert empty_list.find(3) is None


def test_find_non_empty_list_nodes(non_empty_ordered_list):
    searched_node = non_empty_ordered_list.find(1)
    assert searched_node is not None
    assert searched_node.data == 1

    searched_node = non_empty_ordered_list.find(2)
    assert searched_node is not None
    assert searched_node.data == 2

    searched_node = non_empty_ordered_list.find(3)
    assert searched_node is not None
    assert searched_node.data == 3


def test_delete_entire_list(non_empty_ordered_list):
    assert len(non_empty_ordered_list) != 0  # assert list is not empty

    # starting removing nodes from list
    assert non_empty_ordered_list.delete(1) is True
    assert non_empty_ordered_list.find(1) is None

    assert non_empty_ordered_list.delete(2) is True
    assert non_empty_ordered_list.find(2) is None

    assert non_empty_ordered_list.delete(3) is True
    assert non_empty_ordered_list.find(3) is None

    assert len(non_empty_ordered_list) == 0
    assert non_empty_ordered_list.head is None


def test_delete_empty_list_node(empty_list):
    assert empty_list.find(data=1) is None  # assert data not in list
    assert empty_list.delete(data=1) is None


def test_delete_only_head_element_of_linked_list(non_empty_ordered_list):
    assert non_empty_ordered_list.delete(data=1) is True
    assert non_empty_ordered_list.find(data=1) is None


def test_delete_only_tail_element_of_linked_list(non_empty_ordered_list):
    assert non_empty_ordered_list.delete(data=3) is True
    assert non_empty_ordered_list.find(data=3) is None


def test_get_empty_list_all_data(empty_list):
    assert len(empty_list.get_all_data()) == 0


def test_get_non_empty_list_all_data(non_empty_ordered_list):
    non_empty_list_data = non_empty_ordered_list.get_all_data()
    assert len(non_empty_list_data) == 3
    for list_data, test_data in zip(non_empty_list_data, [1, 2, 3, 4]):
        assert list_data == test_data


def test_list_length_calculation(empty_list):
    assert len(empty_list) == 0

    for cont in range(1, 10):
        empty_list.append_head(data=cont)
        assert len(empty_list) == cont


def test_find_kth_element_of_a_list():
    """
    Test case to find the kth element of a list.
    """
    new_list = LinkedList()
    # populate list with data from 1 to 10
    for i in range(1, 11):
        new_list.append(data=i)

    assert new_list.find_kth_element(k=0) == 10
    assert new_list.find_kth_element(k=1) == 9
    assert new_list.find_kth_element(k=2) == 8
    assert new_list.find_kth_element(k=9) == 1
    assert new_list.find_kth_element(k=10) is None


def test_is_palindrome():
    palindromes = ['ana', 'radar', 'renner', 'bob', 'otto', 'madam']
    not_palindromes = ['anaa', 'radara', 'bobb', 'ottoo', 'madama']

    for palindrome in palindromes:
        new_list = LinkedList()
        for letter in palindrome:
            new_list.append(data=letter)
        assert new_list.is_palindrome() is True

    for palindrome in not_palindromes:
        new_list = LinkedList()
        for letter in palindrome:
            new_list.append(data=letter)
        assert new_list.is_palindrome() is False


def test_remove_duplicates():
    new_list = LinkedList()

    for _ in range(10):
        for i in range(1, 11):
            new_list.append(data=i)

    # assert list has duplicates
    assert len(new_list) != len(set(new_list.get_all_data()))
    # call remove duplicates method
    new_list.remove_duplicates()
    # assert list has no more duplicates nodes
    assert len(new_list) == len(set(new_list.get_all_data()))
