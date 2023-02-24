from typing import Optional, List
from utils import raise_data_is_none


class Node:
    def __init__(self, data: int, next_node: Optional['Node'] = None):
        self.data = data
        self.next = next_node

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f'Node({self.data})'


class OrderedList:
    def __init__(self, reverse: bool = False) -> None:
        self.head: Optional[Node] = None
        self._reverse = reverse

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return f'OrderedList({self.head})'

    def _insert_ordered(self, new_node: Node):
        if self.head.data > new_node.data:
            # check if the new node is less than the head if so, make the new node the head
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                if current.next.data > new_node.data:
                    break
                else:
                    # keep searching for the right place to insert a new node
                    # the right place is when the next node is greater than the new node
                    current = current.next

            # check if current is none, insertion at the end
            if current.next is None:
                current.next = new_node
            else:  # insertion in the middle
                new_node.next = current.next
                current.next = new_node

    def _insert_ordered_reversed(self, new_node: Node):
        if self.head.data < new_node.data:
            # check if the new node is less than the head if so, make the new node the head
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                if current.next.data < new_node.data:
                    break
                else:
                    # keep searching for the right place to insert a new node
                    # the right place is when the next node is greater than the new node
                    current = current.next

            # check if current is none, insertion at the end
            if current.next is None:
                current.next = new_node
            else:  # insertion in the middle
                new_node.next = current.next
                current.next = new_node

    @raise_data_is_none
    def append(self, data) -> Node:
        new_node = Node(data=data, next_node=None)

        if self.head is None:
            self.head = new_node
        else:
            if not self._reverse:
                self._insert_ordered(new_node)
            else:
                self._insert_ordered_reversed(new_node)
        return new_node

    @raise_data_is_none
    def find(self, data) -> Optional[Node]:
        if self.head is None:
            return None

        current = self.head
        while current is not None:
            if current.data == data:
                return current

            # if the data is less than the current node, then the data is not in the list
            if not self._reverse:
                if current.data > data:
                    return None
            else:
                # if the data is more than the current node, then the data is not in the list
                if current.data < data:
                    return None
            current = current.next
        return None

    @raise_data_is_none
    def delete(self, data) -> Optional[bool]:
        if self.head is None:
            return None

        # data is not in the head
        if self.head.data == data:
            self.head = self.head.next
            return True

        # search for the data into next nodes, start from the next node from the head
        current = self.head.next
        previous = self.head
        while current is not None:
            if current.data == data:
                previous.next = current.next
                del current
                return True

            previous = current
            current = current.next
        return False

    def print_list(self) -> None:
        if self.head is None:
            print('Empty List')
            return

        current = self.head
        while current is not None:
            if current.next is not None:
                print(current, end=' -> ')
            else:
                print(current)
            current = current.next

    def get_all_data(self) -> List:
        if self.head is None:
            return []

        current = self.head
        data = []
        while current is not None:
            data.append(current.data)
            current = current.next
        return data
