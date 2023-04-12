# Problem: Find the shortest path between two nodes in a graph.

from graphs_trees.graph.graph import Graph


class ShortestPath:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited = set()
        self.queue = []
        self.path = []

    def find_shortest_path(self, start: int, end: int):
        self._find_shortest_path(start, end)
        return self.path

    def _find_shortest_path(self, start: int, end: int):
        self.visited.add(start)
        self.queue.append(start)
        if start == end:
            self.path = self.queue.copy()
            return
        for node in self.graph.nodes[start].adj_nodes.values():
            if node.value not in self.visited:
                self._find_shortest_path(node.value, end)
                if self.path:
                    return
        self.queue.pop()
