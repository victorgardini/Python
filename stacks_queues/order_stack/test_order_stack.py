import pytest
from stack import Stack


@pytest.mark.parametrize('data', [
    ([1, 2, 3, 4, 5]),
    ([3, 5, 7, 9, 11]),
    ([2, 4, 1, 10, 3]),
])
def test_stack(data):
    stack = Stack()

    for d in data:
        stack.push(d)

    sorted_stack = stack.sort_stack()

    sorted_values = []
    while not sorted_stack.is_empty():
        sorted_values.append(sorted_stack.pop())

    assert sorted_values == sorted(data, reverse=True)


if __name__ == '__main__':
    test_stack([1, 2, 3, 4, 5])
