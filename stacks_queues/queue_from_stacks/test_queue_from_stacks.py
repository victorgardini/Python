import pytest

from queue_from_stacks import Queue


@pytest.fixture
def empty_queue():
    return Queue()


def test_dequeue_from_empty_stack(empty_queue):
    assert empty_queue.dequeue() is None


def test_enqueue_on_empty_stack(empty_queue):
    empty_queue.enqueue(1)
    assert not empty_queue.is_empty()
    assert empty_queue.dequeue() == 1


def test_multiple_enqueue_dequeue(empty_queue):
    for i in range(1, 4):  # 1, 2, 3
        empty_queue.enqueue(i)

    for i in range(1, 4):
        assert empty_queue.dequeue() == i


def test_enqueue_after_dequeue(empty_queue):
    empty_queue.enqueue(5)
    assert empty_queue.dequeue() == 5
