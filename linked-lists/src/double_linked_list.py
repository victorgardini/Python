from typing import Optional, List


class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.previous = prev_node

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f'Node(data={self.data})'


class DoubleLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return f'DoubleLinkedList(head={self.head})'

    def append(self, data) -> Node:
        new_node = Node(data=data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node
            new_node.previous = current

        return new_node

    def append_tail(self, data) -> Node:
        new_node = Node(data=data)

        if self.head:
            new_node.next = self.head
            new_node.previous = self.head.previous
            new_node.previous.next = new_node
            new_node.next.previous = new_node
        else:
            self.head = new_node

        return new_node

    def append_head(self, data) -> Node:
        new_node = Node(data=data)

        if self.head:
            new_node.next = self.head
            self.head.previous = new_node

        self.head = new_node
        return new_node

    def find(self, value) -> Optional[Node]:
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next

        return None

    def remove(self, value) -> None:
        node = self.find(value)  # reutilize find method
        if node:
            if node.previous:
                node.previous.next = node.next
            else:  # head node
                self.head = node.next

            if node.next:
                node.next.previous = node.previous

    def print_list(self) -> None:
        if not self.head:
            print('Empty List')
            return

        current = self.head
        while current:
            print(f'Current({current})', end='')
            if current.previous:
                print(f': Previous: {current.previous}', end='')
            if current.next:
                print(f', Next: {current.next}', end='')

            print('')
            current = current.next

    def get_all_data(self) -> List:
        """
        Return a Python List with all the data in the LinkedList.
        """
        data = []
        current = self.head
        while current:
            data.append(current.data)
            current = current.next
        return data
