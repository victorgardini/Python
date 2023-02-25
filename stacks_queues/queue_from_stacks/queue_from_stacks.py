# Problem: Implement a queue using two stacks.

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

        old_top = self.top
        top_data = old_top.data
        del old_top
        self.top = self.top.next

        return top_data

    def peek(self) -> Optional[int]:
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None


class Queue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, data) -> None:
        self.enqueue_stack.push(data)

    def dequeue(self) -> Optional[int]:
        if self.dequeue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def peek(self) -> Optional[int]:
        if self.dequeue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.peek()

    def is_empty(self) -> bool:
        return self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty()
