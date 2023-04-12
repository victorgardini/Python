from graphs_trees.graph_sorted_path.shortest_path import ShortestPath
from graphs_trees.graph.graph import Graph

import pytest


@pytest.fixture
def graph():
    return Graph()


def test_shortest_path(graph):
    graph.add_edge(1, 2, weight=5)
    graph.add_edge(1, 3, weight=3)
    graph.add_edge(1, 5, weight=2)
    graph.add_edge(2, 4, weight=2)
    graph.add_edge(3, 2, weight=1)
    graph.add_edge(3, 4, weight=1)
    graph.add_edge(4, 1, weight=1)
    graph.add_edge(4, 7, weight=2)
    graph.add_edge(4, 8, weight=1)
    graph.add_edge(5, 1, weight=1)
    graph.add_edge(5, 8, weight=4)
    graph.add_edge(5, 9, weight=7)
    graph.add_edge(6, 2, weight=3)
    graph.add_edge(6, 7, weight=1)
    graph.add_edge(7, 3, weight=3)
    graph.add_edge(7, 9, weight=2)
    graph.add_edge(8, 3, weight=2)
    graph.add_edge(8, 6, weight=2)
    graph.add_edge(8, 7, weight=2)

    shortest_path = ShortestPath(graph)

    assert shortest_path.find_shortest_path(1, 9) == [1, 2, 4, 7, 9]


def test_shortest_path_two(graph):
    graph.add_edge(1, 2, weight=7)
    graph.add_edge(2, 3, weight=6)
    graph.add_edge(3, 4, weight=5)
    graph.add_edge(4, 1, weight=6)

    shortest_path = ShortestPath(graph)

    result = shortest_path.find_shortest_path(1, 3)

    assert result == [1, 2, 3]
