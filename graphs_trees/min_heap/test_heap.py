from graphs_trees.min_heap.min_heap import MinHeap
import pytest


@pytest.fixture()
def heap():
    return MinHeap()


def test_min_heap(heap):
    assert heap.peek_min() is None
    assert heap.extract_min() is None

    heap.insert(20)
    assert heap.heap[0] == 20

    heap.insert(5)
    assert heap.heap[0] == 5
    assert heap.heap[1] == 20

    heap.insert(15)
    assert heap.heap[0] == 5
    assert heap.heap[1] == 20
    assert heap.heap[2] == 15

    heap.insert(22)
    assert heap.heap[0] == 5
    assert heap.heap[1] == 20
    assert heap.heap[2] == 15
    assert heap.heap[3] == 22

    heap.insert(40)
    assert heap.heap[0] == 5
    assert heap.heap[1] == 20
    assert heap.heap[2] == 15
    assert heap.heap[3] == 22
    assert heap.heap[4] == 40

    heap.insert(3)
    assert heap.heap[0] == 3
    assert heap.heap[1] == 20
    assert heap.heap[2] == 5
    assert heap.heap[3] == 22
    assert heap.heap[4] == 40
    assert heap.heap[5] == 15

    min_values = [heap.extract_min() for _ in range(6)]
    assert min_values == [3, 5, 15, 20, 22, 40]
