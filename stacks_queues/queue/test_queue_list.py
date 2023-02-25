import pytest
from queue_list import Queue


@pytest.fixture
def queue():
    return Queue()


def test_dequeue_an_empty_queue(queue):
    assert queue.dequeue() is None


def test_enqueue_an_empty_queue_and_dequeue_one_element(queue):
    queue.enqueue(1)
    assert queue.head.data == 1
    assert queue.dequeue() == 1


def test_enqueue_an_empty_queue_and_dequeue_many_elements(queue):
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
