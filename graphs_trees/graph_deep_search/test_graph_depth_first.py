from graphs_trees.graph_deep_search.graph_depth_first import DeepSearchGraph
from graphs_trees.graph.graph import State

import pytest


@pytest.fixture
def graph():
    return DeepSearchGraph()


def test_dfs(graph):
    nodes = []

    for value in range(0, 6):
        nodes.append(graph.add_node(value))

    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 4, 3)
    graph.add_edge(0, 5, 2)
    graph.add_edge(1, 3, 5)
    graph.add_edge(1, 4, 4)
    graph.add_edge(2, 1, 6)
    graph.add_edge(3, 2, 7)
    graph.add_edge(3, 4, 8)

    graph.deep_first_search(0)

    assert nodes[0].state == State.VISITED
    assert nodes[1].state == State.VISITED
    assert nodes[2].state == State.VISITED
    assert nodes[3].state == State.VISITED
    assert nodes[4].state == State.VISITED
    assert nodes[5].state == State.VISITED
