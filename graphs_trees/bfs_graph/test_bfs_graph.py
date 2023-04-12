from graphs_trees.bfs_graph.bfs_graph import GraphBfs, State

import pytest


@pytest.fixture
def graph():
    graph = GraphBfs()
    for key in range(0, 6):
        graph.add_node(key)
    return graph


def test_bfs_graph(graph):
    graph.add_edge(0, 1, weight=5)
    graph.add_edge(0, 4, weight=3)
    graph.add_edge(0, 5, weight=2)
    graph.add_edge(1, 3, weight=5)
    graph.add_edge(1, 4, weight=4)
    graph.add_edge(2, 1, weight=6)
    graph.add_edge(3, 2, weight=7)
    graph.add_edge(3, 4, weight=8)

    graph.bfs(0)

    assert graph.nodes[0].state == State.VISITED