# Problem: Invert a binary tree.

from graphs_trees.binary_tree.binary_tree import BinaryTree


class InvertTree(BinaryTree):

    def invert(self):
        self._invert(self.root)

    def _invert(self, node):
        if node is None:
            return

        self._invert(node.left)
        self._invert(node.right)

        node.left, node.right = node.right, node.left
