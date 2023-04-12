# Problem: Determine if a tree is a valid binary search tree.

from graphs_trees.binary_tree.binary_tree import BinaryTree, Node


class Solution(BinaryTree):

    def is_valid(self) -> bool:
        """ Determine if a tree is a valid binary search tree. """
        if self.root is None:
            raise ValueError('Tree is empty')
        return self._is_valid_tree(self.root)

    def _is_valid_tree(self, node: Node) -> bool:
        """ Determine if a tree is a valid binary search tree. """
        if node.left is not None:
            if node.left.data > node.data:
                return False
            return self._is_valid_tree(node.left)
        if node.right is not None:
            if node.right.data < node.data:
                return False
            return self._is_valid_tree(node.right)
        return True
