# Memento is a behavioral design pattern that allows making snapshots of an object’s state and restoring it in future.

class Originator:
    """
    The Originator holds some important state that may change over time. It also
    defines a method for saving the state inside a memento and another method
    for restoring the state from it.
    """

    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def save_state_to_memento(self):
        return Memento(self._state)

    def restore_state_from_memento(self, memento):
        self._state = memento.get_saved_state()


class Memento:
    """
    The Memento provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it doesn't expose the Originator's
    state.
    """
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state


class Caretaker:
    """
    Classe que é responsável por armazenar e restaurar os estados dos Originators usando o Memento.
    """
    def __init__(self, originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        self._mementos.append(self._originator.save_state_to_memento())

    def undo(self):
        if not self._mementos:
            return

        memento = self._mementos.pop()
        self._originator.restore_state_from_memento(memento)

    def show_history(self):
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_saved_state())


if __name__ == "__main__":
    originator = Originator("State #1")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.set_state("State #2")
    caretaker.backup()
    originator.set_state("State #3")
    caretaker.backup()
    originator.set_state("State #4")

    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    caretaker.show_history()
