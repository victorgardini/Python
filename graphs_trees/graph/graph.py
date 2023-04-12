# Problem: Implement a graph.

from enum import Enum


class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Node:
    def __init__(self, value: int):
        self.value = value
        self.state = State.UNVISITED
        self.incoming_edges = 0
        self.adj_nodes = {}
        self.adj_weights = {}

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def __lt__(self, other: 'Node') -> bool:
        return self.value < other.value

    def add_neighbor(self, node: 'Node', weight=0):
        node.incoming_edges += 1
        self.adj_weights[node.value] = weight
        self.adj_nodes[node.value] = node

    def remove_neighbor(self, node: 'Node'):
        node.incoming_edges -= 1
        del self.adj_weights[node.value]
        del self.adj_nodes[node.value]


class Graph:
    def __init__(self):
        self.nodes = {}  # key: value, value: Node
        self.num_nodes = 0

    def __repr__(self):
        return str(self.nodes)

    def __str__(self):
        return str(self.nodes)

    def add_node(self, value: int) -> Node:
        if value not in self.nodes:
            self.nodes[value] = Node(value)
            self.num_nodes += 1
        return self.nodes[value]

    def add_edge(self, source_key: int, dest_key: int, weight=0):
        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key], weight)

    def add_undirected_edge(self, source_key: int, dest_key: int, weight=0):
        self.add_edge(source_key, dest_key, weight)
        self.add_edge(dest_key, source_key, weight)
