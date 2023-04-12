# Problem: Find the second-largest node in a binary search tree.

from graphs_trees.binary_tree.binary_tree import BinaryTree, Node


class Solution(BinaryTree):

    def find_second_largest_node(self) -> int:
        """ Find the second largest node in a binary search tree. """
        if self.root is None:
            raise ValueError('Tree is empty')
        return self._find_second_largest_node(self.root)

    def _find_second_largest_node(self, node: Node) -> int:
        """ Find the second largest node in a binary search tree. """
        if node.right is None:
            if node.left is None:
                raise ValueError('Tree has only one node')
            return self._find_max(node.left)
        if node.right.right is None and node.right.left is None:
            return node.data
        return self._find_second_largest_node(node.right)

    def find_max(self) -> int:
        """ Find the largest node in a binary search tree. """
        if self.root is None:
            raise ValueError('Tree is empty')
        return self._find_max(self.root)

    def _find_max(self, node: Node) -> int:
        """ Find the largest node in a binary search tree. """
        if node.right is None:
            return node.data
        return self._find_max(node.right)
