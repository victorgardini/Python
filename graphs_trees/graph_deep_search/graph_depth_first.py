# Problem: Implement depth-first search on a graph.

from graphs_trees.graph.graph import Graph, State


class DeepSearchGraph(Graph):

    def deep_first_search(self, start):
        if start is None:
            return

        self.nodes[start].state = State.VISITED
        for node in self.nodes[start].adj_nodes.values():
            if node.state == State.UNVISITED:
                self.deep_first_search(node.value)
