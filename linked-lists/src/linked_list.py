from typing import Optional, List
from .utils import raise_data_is_none


class Node:
    def __init__(self, data, next_node: Optional['Node'] = None) -> None:
        self.data = data
        self.next = next_node

    def __str__(self):
        return f'{str(self.data)}'

    def __repr__(self):
        return f'Node({self.data})'


class LinkedList:
    """
    Data Structure implementation of a Linked List.
    """
    def __init__(self, head=None) -> None:
        self.head: Optional[Node] = head

    @raise_data_is_none
    def append_head(self, data) -> Node:
        """
        Challenge: insert a new node at the head of the list.
        :param data: data to be inserted.
        :return: created node.
        """

        # Create a new node and insert into head of LinkedList
        new_node = Node(data=data, next_node=None)
        if self.head is not None:
            new_node.next = self.head

        self.head = new_node
        return new_node

    @raise_data_is_none
    def append(self, data) -> Node:
        """
        Challenge: insert a new node at the tail of the list.
        :param data:
        :return: created node.
        """
        # Create a new node and insert into tail of LinkedList
        new_node = Node(data=data, next_node=None)
        if self.head is None:  # new head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # search for the end of list
                current = current.next

            # change last node
            current.next = new_node

        # return created node
        return new_node

    @raise_data_is_none
    def find(self, data) -> Optional[Node]:
        """
        Challenge: find a node in the list.
        :param data: data to be found.
        :return: found node, or None if not found.
        """
        if self.head:
            current = self.head
            while current is not None:
                if current.data == data:
                    return current
                current = current.next

        # not found
        return None

    @raise_data_is_none
    def delete(self, data) -> Optional[bool]:
        """
        Challenge: delete a node from the list that contains the given data.
        :param data: Node data to be deleted.
        :return: True if deleted, False if not found, None if list is empty.
        """
        if not self.head:
            return None

        # delete head
        if self.head.data == data:
            delete_node = self.head
            self.head = delete_node.next
            del delete_node
            return True

        previous_node = self.head
        current_node = self.head.next

        while current_node is not None:
            if current_node.data == data:
                previous_node.next = current_node.next
                del current_node
                return True

            previous_node = current_node
            current_node = current_node.next

        return False

    def print_list(self) -> None:
        if self.head is None:
            print('Empty List')
            return

        current = self.head
        while current:
            if current.next:
                print(current, end=' -> ')
            else:
                print(current)
            current = current.next

    def get_all_data(self) -> List:
        """
        Return a Python List with all the data in the LinkedList.
        """
        data = []
        current = self.head
        while current is not None:
            data.append(current.data)
            current = current.next
        return data

    def __len__(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
