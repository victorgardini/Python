# Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain
# of handlers. Upon receiving a request, each handler decides either to process the request or
# to pass it to the next handler in the chain.

from abc import ABC, abstractmethod


class Handler(ABC):
    """
    The Handler interface could declare a method for building the chain of handlers.
    It also declares a method for executing a request.
    In this case, the setup of next handler is done when the instance is created.
    """

    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, request):
        pass


class ConcreteHandlerA(Handler):
    """
    All Concrete Handlers either handle a request or pass it to the next handler in
    the chain.
    """
    def handle(self, request):
        if request == "A":
            print("ConcreteHandlerA: Handling request")
        elif self._successor is not None:
            self._successor.handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("ConcreteHandlerB: Handling request")
        elif self._successor is not None:
            self._successor.handle(request)


class ConcreteHandlerC(Handler):
    def handle(self, request):
        if request == "C":
            print("ConcreteHandlerC: Handling request")
        elif self._successor is not None:
            self._successor.handle(request)


if __name__ == "__main__":
    handler_c = ConcreteHandlerC()
    handler_b = ConcreteHandlerB(handler_c)
    handler_a = ConcreteHandlerA(handler_b)

    handler_a.handle("A")
    handler_a.handle("B")
    handler_a.handle("C")
