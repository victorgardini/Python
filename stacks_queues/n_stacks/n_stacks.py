# Problem: Implement n stacks using a single array.

class Stack:
    def __init__(self, stack_number, stack_size):
        self.stack_number = stack_number
        self.stack_size = stack_size

        # Initialize stack pointers to -1 to indicate that the stacks are empty.
        self.stack_pointers = [-1] * stack_number  # ex: [-1, -1, -1]

        # Initialize Stack Array ex: [None, None, None, None, None, None, None, None, None]
        self.stack_array = [None] * stack_size * stack_number

    def push(self, stack_index, data):
        if self.is_full(stack_index):
            raise Exception("Stack is full.")

        self.stack_pointers[stack_index] += 1  # Increment stack pointer
        array_index = self.get_top_index(stack_index)  # Get top index of stack 'sn' after incrementing stack pointer
        self.stack_array[array_index] = data  # Update array

    def get_top_index(self, stack_index):
        """
        Returns the index of the top of the stack. If the stack is empty, returns the index of the bottom of the stack.
        This index is calculated using the formula: (stack_index * stack_size) + stack_pointer

        :param stack_index: The index of the stack.
        :return: The index of the top of the stack.
        """
        offset = stack_index * self.stack_size  # Offset to the start of the stack
        return self.stack_pointers[stack_index] + offset

    def pop(self, stack_index):
        if self.is_empty(stack_index):
            raise Exception("Stack is empty.")

        # Get top index of stack 'sn' before decrementing stack pointer to avoid index out
        # of bounds error in case of stack size 1 and stack pointer 0 (i.e. stack is empty)
        # and we try to access the array at index -1.
        top_index = self.get_top_index(stack_index)
        data = self.stack_array[top_index]  # Get top of stack 'sn' from array before decrementing stack pointer
        self.stack_array[top_index] = None  # Clear data
        self.stack_pointers[stack_index] -= 1  # Decrement stack pointer
        return data

    def is_full(self, stack_index):
        return self.stack_pointers[stack_index] == self.stack_size - 1  # Stack is full if stack pointer is at the end

    def is_empty(self, stack_index):
        return self.stack_pointers[stack_index] == -1  # Stack is empty if stack pointer is at the beginning
