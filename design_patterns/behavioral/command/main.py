# Command is behavioral design pattern that converts requests or simple operations into objects.

from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class AddCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """
    def __init__(self, receiver: 'Receiver', value):
        self._receiver = receiver
        self._value = value

    def execute(self):
        self._receiver.add(self._value)

    def undo(self):
        self._receiver.remove(self._value)


class Receiver:
    """
    The Receiver classes contain some important business logic. They know how to
    perform all kinds of operations, associated with carrying out a request. In
    fact, any class may serve as a Receiver.
    """
    def __init__(self):
        self._data = []

    def add(self, value):
        self._data.append(value)
        print(f"Receiver: Added {value}. Data is now {self._data}")

    def remove(self, value):
        self._data.remove(value)
        print(f"Receiver: Removed {value}. Data is now {self._data}")


class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    """

    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

    def undo_last_command(self):
        if self._commands:
            command = self._commands.pop()
            command.undo()


if __name__ == "__main__":
    receiver = Receiver()  # Receiver is the target of the command
    add_command_1 = AddCommand(receiver, 10)  # Command is the encapsulated request
    add_command_2 = AddCommand(receiver, 20)  # Command is the encapsulated request

    invoker = Invoker()  # Invoker holds the command
    invoker.add_command(add_command_1)  # Added command to invoker
    invoker.add_command(add_command_2)  # Added command to invoker

    invoker.execute_commands()  # Invoker executes the command

    invoker.undo_last_command()
