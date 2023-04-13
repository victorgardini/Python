# Problem: Find a build order given a list of projects and dependencies.

# I cannot solve this problem. I am not sure how to use the graph data structure to solve this problem.
# Maybe i'm so tired that I cannot think of a solution.
# todo: I will come back to this problem later.

from typing import List
from graphs_trees.graph.graph import Graph


class CustomGraph(Graph):

    def topological_sort(self):
        sorted_nodes = []
        nodes = self.nodes.values()
        for node in nodes:
            if node.incoming_edges == 0:
                sorted_nodes.append(node)

        while sorted_nodes:
            node = sorted_nodes.pop()
            for adj_node in node.adj_nodes.values():
                adj_node.incoming_edges -= 1
                if adj_node.incoming_edges == 0:
                    sorted_nodes.append(adj_node)

        return [node.value for node in nodes]


class Dependency:
    def __init__(self, project, dependency):
        self.after = project
        self.before = dependency


class BuildOrder:
    def __init__(self, dependencies: List[Dependency], name: str):
        self.graph = CustomGraph()
        self.name = name
        self.dependencies = dependencies
        self.build_order = []

    def find_build_order(self):
        for dependency in self.dependencies:
            self.graph.add_edge(dependency.after, dependency.before)
        self.build_order = self.graph.topological_sort()
        return self.build_order
