# Mediator is a behavioral design pattern that reduces coupling between components of a program
# by making them communicate indirectly, through a special mediator object.

from abc import ABC, abstractmethod
from typing import List


class Mediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    @abstractmethod
    def send_message(self, message: str, sender: 'Colleague'):
        pass


class Colleague(ABC):
    """
    The Colleague provides the basic functionality of storing a mediator's
    instance inside component objects.
    """

    def __init__(self, mediator: Mediator):
        self._mediator = mediator

    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self, message: str):
        pass


"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""


class ConcreteColleague1(Colleague):
    """
    Concrete Colleagues are classes that communicate with each other, but they
    still have to do so via a mediator object. It prevents them from referring
    to each other directly.
    """

    def send(self, message: str):
        print(f"Colleague 1 sends message: {message}")
        self._mediator.send_message(message, self)

    def receive(self, message: str):
        print(f"Colleague 1 receives message: {message}")


class ConcreteColleague2(Colleague):
    def send(self, message: str):
        print(f"Colleague 2 sends message: {message}")
        self._mediator.send_message(message, self)

    def receive(self, message: str):
        print(f"Colleague 2 receives message: {message}")


class ConcreteMediator(Mediator):
    """
    Concrete Mediators implement cooperative behavior by coordinating several
    components.
    """

    def __init__(self):
        self._colleagues: List[Colleague] = []

    def add_colleague(self, colleague: Colleague):
        self._colleagues.append(colleague)

    def send_message(self, message: str, sender: Colleague):
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(message)


if __name__ == "__main__":
    mediator = ConcreteMediator()  # Create mediator
    colleague1 = ConcreteColleague1(mediator)  # Create colleagues
    colleague2 = ConcreteColleague2(mediator)  # Create colleagues

    mediator.add_colleague(colleague1)  # Add colleagues to mediator
    mediator.add_colleague(colleague2)  # Add colleagues to mediator

    colleague1.send("Hello, colleague 2!")  # Send message
    colleague2.send("Hi, colleague 1!")  # Send message

