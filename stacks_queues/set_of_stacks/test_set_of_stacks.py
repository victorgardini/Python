import pytest
from set_of_stacks import SetOfStacks


@pytest.fixture
def set_stack():
    return SetOfStacks(individual_stack_capacity=3)


@pytest.fixture
def set_stack_full():
    set_stack = SetOfStacks(individual_stack_capacity=3)
    for i in range(3):
        set_stack.push(data=i)
    return set_stack


def test_push_on_an_empty_stack(set_stack):
    set_stack.push(1)
    assert set_stack.peek() == 1


def test_push_on_a_non_empty_stack(set_stack):
    set_stack.push(1)
    set_stack.push(2)


def test_push_on_a_full_stack_to_create_a_new_one(set_stack_full):
    assert set_stack_full._stacks[0].is_full()
    assert len(set_stack_full._stacks) == 1

    set_stack_full.push(data=3)
    assert len(set_stack_full._stacks) == 2


def test_pop_on_an_stack_to_destroy_it(set_stack_full):
    set_stack_full.push(data=4)  # create a new stack

    assert set_stack_full._stacks[0].is_full()
    assert len(set_stack_full._stacks) == 2

    set_stack_full.pop()  # destroy the last stack
    assert len(set_stack_full._stacks) == 1


def test_pop_on_an_empty_stack(set_stack):
    assert set_stack.pop() is None
