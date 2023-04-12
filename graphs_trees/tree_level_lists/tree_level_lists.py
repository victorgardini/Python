# Problem: Create a list for each level of a binary tree.

from graphs_trees.binary_tree.binary_tree import BinaryTree
from typing import List, Optional


class TreeLevelLists(BinaryTree):

    def create_level_lists(self) -> Optional[List[List[int]]]:
        if self.root is None:
            return None

        result = []
        current = [self.root]

        while current:  # while there are nodes to process
            result.append(current)  # add current level
            parents = current  # go to next level
            current = []  # reset current
            for node in parents:  # for each parent
                if node.left:  # add children to current
                    current.append(node.left)
                if node.right:  # add children to current
                    current.append(node.right)

        # extract values from nodes
        return [[node.data for node in level] for level in result]
