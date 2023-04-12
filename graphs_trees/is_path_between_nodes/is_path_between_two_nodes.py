# Problem: Determine whether there is a path between two nodes in a graph.

from graphs_trees.graph.graph import Graph, State
from collections import deque


class Solution(Graph):

    def path_exists(self, start: int, end: int) -> bool:
        if start == end:
            return True

        # Get the start and end nodes.
        start_node = self.nodes[start]
        end_node = self.nodes[end]

        # Create a queue and enqueue the start node.
        queue = deque()
        queue.append(start_node)
        start_node.state = State.VISITING  # Mark the start node as visiting.

        # While the queue is not empty.
        while queue:
            node = queue.popleft()  # Dequeue the first node.
            if node is end_node:  # If the node is the end node, return True because we found a path.
                return True
            for neighbor in node.adj_nodes.values():  # For each neighbor.
                # If the neighbor is unvisited, meaning we haven't visited it yet.
                if neighbor.state == State.UNVISITED:
                    queue.append(neighbor)  # Enqueue the neighbor.
                    neighbor.state = State.VISITING  # Mark the neighbor as visiting.
            node.state = State.VISITED  # Mark the node as visited, because we have visited it.

        # If we get here, it means we didn't find a path, so return False.
        return False
