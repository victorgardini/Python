from graphs_trees.graph.graph import Graph, Node

import pytest


@pytest.fixture
def graph():
    graph = Graph()
    for key in range(0, 6):
        graph.add_node(key)
    return graph


def test_graph(graph):
    graph.add_edge(0, 1, weight=5)
    graph.add_edge(0, 5, weight=2)
    graph.add_edge(1, 2, weight=3)
    graph.add_edge(2, 3, weight=4)
    graph.add_edge(3, 4, weight=5)
    graph.add_edge(3, 5, weight=6)
    graph.add_edge(4, 0, weight=7)
    graph.add_edge(5, 4, weight=8)
    graph.add_edge(5, 2, weight=9)

    assert graph.nodes[0].adj_weights[graph.nodes[1].value] == 5
    assert graph.nodes[0].adj_weights[graph.nodes[5].value] == 2
    assert graph.nodes[1].adj_weights[graph.nodes[2].value] == 3
    assert graph.nodes[2].adj_weights[graph.nodes[3].value] == 4
    assert graph.nodes[3].adj_weights[graph.nodes[4].value] == 5
    assert graph.nodes[3].adj_weights[graph.nodes[5].value] == 6
    assert graph.nodes[4].adj_weights[graph.nodes[0].value] == 7
    assert graph.nodes[5].adj_weights[graph.nodes[4].value] == 8
    assert graph.nodes[5].adj_weights[graph.nodes[2].value] == 9

    assert graph.nodes[0].incoming_edges == 1
    assert graph.nodes[1].incoming_edges == 1
    assert graph.nodes[2].incoming_edges == 2
    assert graph.nodes[3].incoming_edges == 1
    assert graph.nodes[4].incoming_edges == 2
    assert graph.nodes[5].incoming_edges == 2

    graph.nodes[0].remove_neighbor(graph.nodes[1])

    assert graph.nodes[1].incoming_edges == 0
    graph.nodes[3].remove_neighbor(graph.nodes[4])

    assert graph.nodes[4].incoming_edges == 1
    assert (graph.nodes[0] < graph.nodes[1]) is True


def test_graph_undirected(graph):
    graph.add_undirected_edge(0, 1, weight=5)
    graph.add_undirected_edge(0, 5, weight=2)
    graph.add_undirected_edge(1, 2, weight=3)

    assert graph.nodes[0].adj_weights[graph.nodes[1].value] == 5
    assert graph.nodes[1].adj_weights[graph.nodes[0].value] == 5
    assert graph.nodes[0].adj_weights[graph.nodes[5].value] == 2
    assert graph.nodes[5].adj_weights[graph.nodes[0].value] == 2
    assert graph.nodes[1].adj_weights[graph.nodes[2].value] == 3
    assert graph.nodes[2].adj_weights[graph.nodes[1].value] == 3
