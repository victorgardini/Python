# Problem: Implement a binary tree

# This implementation is based on the following article:
# - https://www.geeksforgeeks.org/introduction-to-binary-tree-data-structure-and-algorithm-tutorials/

from typing import Optional, List


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f'Node(data={self.data}, l={self.left}, r={self.right})'


class BinaryTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return f'BinaryTree(root={self.root})'

    def insert(self, data):
        """ Basic Operation: Inserting an element. """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)  # insert recursively

    def _insert(self, node: Node, data) -> None:
        """ Insert a node into the tree, recursively. """
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def remove(self, data):
        """ Basic Operation: Removing an element. """
        if self.root is not None:
            self.root = self._remove(self.root, data)

    def _remove(self, node: Node, data) -> Optional[Node]:
        """ Remove a node from the tree, recursively. """
        if node is None:
            return None

        if data < node.data:  # Go to the left
            node.left = self._remove(node.left, data)
        elif data > node.data:  # Go to the right
            node.right = self._remove(node.right, data)
        else:  # Found the node to remove
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.data = self._find_min(node.right)
                node.right = self._remove(node.right, node.data)

        return node

    def _find_min(self, node: Node) -> int:
        """ Find the minimum value in a subtree. """
        if node.left is None:  # Found the minimum (leftmost) node
            return node.data
        else:
            return self._find_min(node.left)

    def find(self, data):
        """ Basic Operation: Finding an element. """
        return self._find(self.root, data)

    def _find(self, node: Node, data) -> bool:
        """ Find a node in the tree, recursively. """
        if node is None:
            return False
        elif data < node.data:
            return self._find(node.left, data)
        elif data > node.data:
            return self._find(node.right, data)
        else:
            return True

    def traverse_in_order(self) -> List[int]:
        """ Basic Operation: Traversing the tree. """
        return self._traverse_in_order(self.root)

    def _traverse_in_order(self, node: Node) -> List[int]:
        """ Traverse the tree in order, recursively. """
        if node is None:
            return []
        else:
            return self._traverse_in_order(node.left) + [node.data] + self._traverse_in_order(node.right)

    def traverse_pre_order(self) -> List[int]:
        """ Basic Operation: Traversing the tree. """
        return self._traverse_pre_order(self.root)

    def _traverse_pre_order(self, node: Node) -> List[int]:
        """ Traverse the tree pre order, recursively. """
        if node is not None:
            return [node.data] + self._traverse_pre_order(node.left) + self._traverse_pre_order(node.right)
        else:
            return []

    def traverse_post_order(self) -> List[int]:
        """ Basic Operation: Traversing the tree. """
        return self._traverse_post_order(self.root)

    def _traverse_post_order(self, node: Node) -> List[int]:
        """ Traverse the tree post order, recursively. """
        if node is not None:
            return self._traverse_post_order(node.left) + self._traverse_post_order(node.right) + [node.data]
        else:
            return []

    @property
    def height(self):
        """ Basic Operation: Get the height of the tree. """
        return self._height(self.root)

    def _height(self, node: Node) -> int:
        """ Get the height of the tree, recursively. """
        if node is None:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    def size(self):
        """ Basic Operation: Get the size of the tree. """
        return self._size(self.root)

    def _size(self, node: Node) -> int:
        """ Get the size of the tree, recursively. """
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def find_level(self, data):
        """ Basic Operation: Find the level of a Node in the tree. """
        return self._find_level(self.root, data)

    def _find_level(self, node: Node, data, level=0) -> int:
        """ Find the level of the tree, recursively. """
        if node is None:
            return -1
        elif data < node.data:
            return self._find_level(node.left, data, level + 1)
        elif data > node.data:
            return self._find_level(node.right, data, level + 1)
        else:
            return level
