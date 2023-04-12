# Problem: Check if a binary tree is balanced.

from graphs_trees.binary_tree.binary_tree import BinaryTree, Node


class Solution(BinaryTree):

    def is_balanced(self) -> bool:
        """ Check if a binary tree is balanced. """
        if self.root is None:
            raise ValueError('Tree is empty')
        return self._is_balanced(self.root)

    def _is_balanced(self, node: Node) -> bool:
        """ Check if a binary tree is balanced. """
        if node is None:
            return True
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self._is_balanced(node.left) and self._is_balanced(node.right)

    def _get_height(self, node: Node) -> int:
        """ Get the height of a binary tree. """
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))
