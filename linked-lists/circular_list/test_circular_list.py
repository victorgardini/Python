from circular_list import CircularLinkedList


def test_circular_list():
    new_list = CircularLinkedList()

    print('>>> Inserting (1), (2) and (3)')
    new_list.append(1)
    new_list.append(2)
    new_list.append(3)
    new_list.append(4)
    new_list.append(5)
    new_list.print_list()

    print('>>> Searching for (5) and (2)')
    print(new_list.find(5))
    print(new_list.find(2))
    new_list.print_list()

    print('>>> Deleting (5) and (2)')
    print(new_list.delete(1))
    print(new_list.delete(2))
    print(new_list.delete(3))
    print(new_list.delete(3))
    print(new_list.delete(4))
    print(new_list.delete(5))
    new_list.print_list()

    print('>>> Inserting (5), (6) and (75)')
    new_list.append(5)
    new_list.append(6)
    new_list.append(75)
    new_list.print_list()


if __name__ == '__main__':
    test_circular_list()
