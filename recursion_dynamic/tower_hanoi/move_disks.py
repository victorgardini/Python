# Problem: Implement the Towers of Hanoi with 3 towers and N disks.


class Stack:
    def __init__(self):
        self.__disk = []

    def push(self, data):
        return self.__disk.append(data)

    def pop(self):
        return self.__disk.pop()


def move_disk(num_disks: int, source: Stack, destination: Stack, buffer: Stack):
    # Base case - move the disk from source to destination
    if num_disks == 1:
        destination.push(source.pop())
    else:
        # Move the top n-1 disks from source to buffer, using destination as a buffer
        move_disk(num_disks - 1, source, buffer, destination)
        move_disk(1, source, destination, buffer)
        move_disk(num_disks - 1, buffer, destination, source)
