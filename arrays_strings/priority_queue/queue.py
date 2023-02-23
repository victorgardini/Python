from typing import List, Optional

import sys


class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __repr__(self):
        return f"Node({self.data}, {self.priority})"


class PriorityQueue:
    def __init__(self):
        self.array: List[Node] = []

    def __repr__(self):
        return f"PriorityQueue({self.array})"

    def __len__(self) -> int:
        return len(self.array)

    def __bool__(self) -> bool:
        return len(self) > 0

    def insert(self, data, priority) -> Node:
        """
        Inserts a new node into the list.
        :param data: data to be stored in the node.
        :param priority: priority of the node.
        :return: None.
        """
        self.array.append(Node(data=data, priority=priority))
        return self.array[-1]

    def remove_min(self) -> Optional[Node]:
        """
        Removes the node with the lowest priority.
        :return: the removed Node.
        """
        if len(self.array) == 0:
            return None

        minimum = sys.maxsize
        min_index = 0
        for index, node in enumerate(self.array):
            if node.priority < minimum:
                minimum = node.priority
                min_index = index

        return self.array.pop(min_index)

    def clear(self) -> None:
        self.array = []

    def contains(self, data) -> bool:
        for node in self.array:
            if node.data == data:
                return True
        return False

    def update_priority(self, data, priority) -> bool:
        for node in self.array:
            if node.data == data:
                node.priority = priority
                return True
        return False
