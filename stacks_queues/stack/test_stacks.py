from stack import Stack
import pytest


@pytest.fixture
def stack():
    return Stack()


def test_empty_stack(stack):
    assert stack.peek() is None
    assert stack.pop() is None


def test_stack_push_one_element(stack):
    stack.push(5)
    assert stack.pop() == 5
    assert stack.peek() is None


def test_stack_push_more_than_one_elements(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.is_empty() is False
    assert stack.pop() == 1
    assert stack.peek() is None
    assert stack.is_empty() is True
