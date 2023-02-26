import pytest
from n_stacks import Stack


@pytest.fixture
def stacks():
    return Stack(3, 3)


def test_pop_on_empty(stacks):
    with pytest.raises(Exception):
        stacks.pop(0)


def test_push_on_full(stacks):
    # Insert 3 elements into stack 0 until it is full (cause stack_size = 3)
    for i in range(0, 3):
        stacks.push(2, i)
    with pytest.raises(Exception):
        stacks.push(2, 3)


def test_push_and_pop_stacks(stacks):
    stacks.push(0, 1)
    stacks.push(0, 2)
    stacks.push(1, 3)
    stacks.push(2, 4)

    assert stacks.pop(0) == 2
    assert stacks.pop(0) == 1
    assert stacks.pop(1) == 3
    assert stacks.pop(2) == 4
