from is_path_between_two_nodes import Solution

import pytest


@pytest.fixture
def graph_with_nodes():
    graph = Solution()
    for value in range(0, 6):
        graph.add_node(value)
    return graph


@pytest.fixture
def graph_with_nodes_and_edges(graph_with_nodes):
    graph_with_nodes.add_edge(0, 1, weight=5)
    graph_with_nodes.add_edge(0, 4, weight=3)
    graph_with_nodes.add_edge(0, 5, weight=2)
    graph_with_nodes.add_edge(1, 3, weight=5)
    graph_with_nodes.add_edge(1, 4, weight=4)
    graph_with_nodes.add_edge(2, 1, weight=6)
    graph_with_nodes.add_edge(3, 2, weight=7)
    graph_with_nodes.add_edge(3, 4, weight=8)
    return graph_with_nodes


def test_there_is_path_between_two_nodes(graph_with_nodes_and_edges):
    assert graph_with_nodes_and_edges.path_exists(0, 2) is True
    assert graph_with_nodes_and_edges.path_exists(0, 0) is True
    assert graph_with_nodes_and_edges.path_exists(4, 5) is False
