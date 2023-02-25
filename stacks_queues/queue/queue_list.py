from typing import Optional


class Node:
    def __init__(self, data: int, next_node: Optional['Node'] = None):
        self.data = data
        self.next = next_node

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f'Node(data={self.data})'


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def enqueue(self, data: int) -> None:
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self) -> Optional[int]:
        if self.head is None and self.tail is None:
            return None

        data = self.head.data  # save the data to return it

        if self.head == self.tail:  # if there is only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return data