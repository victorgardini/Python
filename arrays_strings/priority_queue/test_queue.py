from queue import PriorityQueue

import pytest


def test_queue_empty_queue():
    queue = PriorityQueue()
    assert len(queue) == 0
    assert not queue


def test_remove_min_empty_queue():
    queue = PriorityQueue()
    assert queue.remove_min() is None


@pytest.mark.parametrize("data, priority", [
    ("a", 1),
    ("b", 2),
    ("c", 3),
    ("d", 4),
    ("e", 5),
])
def test_insert(data, priority):
    queue = PriorityQueue()
    node = queue.insert(data, priority)
    assert node.data == data
    assert node.priority == priority
    assert len(queue) == 1
    assert queue


def test_decrease_key():
    queue = PriorityQueue()

    for data, priority in [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]:
        queue.insert(data, priority)

    queue.update_priority("c", 0)  # Decrease the priority of "c" to 0.
    assert queue.remove_min().data == "c"
    assert queue.remove_min().data == "a"
