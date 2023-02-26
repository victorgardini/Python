# Problem: Implement SetOfStacks that wraps a list of stacks, where each stack is bound by a capacity.

from typing import Optional, List


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f'Node(data={self.data}, next={self.next})'


class StackWithCapacity:
    def __init__(self, top=None, capacity=10):
        self.top = top
        self._capacity = capacity
        self._num_items = 0

    def push(self, data) -> None:
        if self.is_full():
            raise Exception('Stack is full')

        self.top = Node(data=data, next=self.top)
        self._num_items += 1

    def pop(self) -> Optional[int]:
        if self.is_empty():
            return None

        old_top = self.top
        top_data = old_top.data
        del old_top
        self.top = self.top.next
        self._num_items -= 1

        return top_data

    def peek(self) -> Optional[int]:
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None

    def is_full(self) -> bool:
        return self._num_items == self._capacity


class SetOfStacks:
    def __init__(self, individual_stack_capacity=10):
        self._stacks: List[StackWithCapacity] = []
        self._individual_stack_capacity = individual_stack_capacity

    def push(self, data) -> None:
        if not self._stacks or self._stacks[-1].is_full():
            self._stacks.append(StackWithCapacity(capacity=self._individual_stack_capacity))

        self._stacks[-1].push(data=data)

    def pop(self) -> Optional[int]:
        if not self._stacks:
            return None

        data = self._stacks[-1].pop()

        if self._stacks[-1].is_empty():
            del self._stacks[-1]

        return data

    def pop_at(self, index: int) -> Optional[int]:
        if not self._stacks or index >= len(self._stacks):
            return None

        data = self._stacks[index].pop()

        if self._stacks[index].is_empty():
            del self._stacks[index]

        return data

    def peek(self) -> Optional[int]:
        if not self._stacks:
            return None

        return self._stacks[-1].peek()

    def is_empty(self) -> bool:
        return not self._stacks

    def __str__(self):
        return str(self._stacks)

    def __repr__(self):
        return f'SetOfStacks(stacks={self._stacks})'
