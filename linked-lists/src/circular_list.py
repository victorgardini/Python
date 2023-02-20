from typing import List, Optional


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return f'Node(data={self.data}, next={self.next.data})'


class CircularLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, data):
        new_node = Node(data=data)

        # head insertion
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
            return new_node

        # tail insertion
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head
        return new_node

    def find(self, data) -> Optional[Node]:
        if self.head is None:
            return None

        end = self.tail
        current = self.head
        while current and current != end:
            if current.data == data:
                return current
            current = current.next
        return None

    def delete(self, data) -> Optional[bool]:
        if not self.head:
            return None

        # check if data is in the head
        if self.head.data == data:
            deleted_node = self.head

            # check if there is only one node remaining
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = deleted_node.next
                self.tail.next = self.head

            del deleted_node  # explicit delete
            return True

        # search for the data into next nodes, start from the next node from the head
        end = self.tail
        current = self.head
        previous = end
        while current:
            if current.data == data:
                break
            if current == end:
                return False
            previous = current
            current = current.next

        # delete the node
        if current.next == self.head:
            self.head = current.next

        previous.next = current.next
        del current  # explicit delete
        return True

    def print_list(self) -> None:
        if not self.head:
            print('Empty List')
            return

        end = self.tail
        current = self.head

        while current:
            print(f'Current: {current.data} -> Next: {current.next.data}')
            current = current.next
            if current == end:
                print(f'Current: {current.data} -> Next: {current.next.data} [END]')
                break

    def get_data(self) -> List:
        if not self.head:
            return []

        start = self.head
        current = self.head.next
        data = [start.data]
        while current:
            if current == start:
                break
            data.append(current.data)
            current = current.next

        return data
