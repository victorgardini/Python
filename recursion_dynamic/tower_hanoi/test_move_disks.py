from move_disks import move_disk, Stack


def test_hanoi():
    num_disks = 3

    # initialize 3 towers
    source = Stack()
    destination = Stack()
    buffer = Stack()

    # push 3 disks onto source tower
    source.push(3)
    source.push(2)
    source.push(1)

    # move disks from source to destination
    move_disk(num_disks, source, destination, buffer)

    # check that disks are in order on destination tower
    assert destination.pop() == 1
    assert destination.pop() == 2
    assert destination.pop() == 3
