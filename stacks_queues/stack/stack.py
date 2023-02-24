# Problem: Implement a stack with push, pop, peek, and is_empty methods using a linked list.

from typing import Optional


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f'Node(data={self.data}, next={self.next})'


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data) -> None:
        self.top = Node(data=data, next=self.top)

    def pop(self) -> Optional[int]:
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next

        return data

    def peek(self) -> Optional[int]:
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None
