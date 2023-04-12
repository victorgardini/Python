# Problem: Implement breadth-first search on a graph.

from graphs_trees.graph.graph import Graph, State

from collections import deque


class GraphBfs(Graph):

    def bfs(self, start_key: int):
        if start_key not in self.nodes:
            return

        start_node = self.nodes[start_key]
        start_node.state = State.VISITING
        queue = deque()
        queue.append(start_node)

        while queue:
            current_node = queue.popleft()
            for node in current_node.adj_nodes.values():
                if node.state == State.UNVISITED:
                    node.state = State.VISITING
                    queue.append(node)
            current_node.state = State.VISITED
