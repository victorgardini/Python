from ordered_list import OrderedList
import pytest


TEST_ORDERED_LIST_REVERSED_CASE = [
    (1, 2, 3, 4, 5),  # inserted data
    (5, 4, 3, 2, 1),  # expected order
]


@pytest.fixture
def non_empty_ordered_list() -> OrderedList:
    ordered_list = OrderedList(reverse=True)
    for item in TEST_ORDERED_LIST_REVERSED_CASE[0]:
        ordered_list.append(item)
    return ordered_list


def test_append_list_reversed_unsure_order_exists(non_empty_ordered_list):
    # test ordered list

    for node_data, expected in zip(non_empty_ordered_list.get_all_data(), TEST_ORDERED_LIST_REVERSED_CASE[1]):
        assert node_data == expected
