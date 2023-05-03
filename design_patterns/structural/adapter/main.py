

class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The Adaptee class contains some useful behavior, but its interface is
    incompatible with the existing client code. The Adaptee needs some
    adaptation before the client code can use it.
    """

    def specific_request(self) -> str:
        """
        Some useful behavior the Adaptee class has.
        In the real world, the Adaptee class may have dozens of useful methods.
        And Adaptee cold return other types of data, eg: dictionaries, not just string.
        """
        return "Request processed by Adaptee"


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def __init__(self, adaptee: Adaptee):
        """
        The Adapter class accepts an object of the Adaptee class via the constructor,
        and stores it in a field.
        """
        self._adaptee = adaptee

    def request(self) -> str:
        """
        The Adapter class redefines the behavior of the Target's request() method
        """
        return f"Adapter: {self._adaptee.specific_request()}"


if __name__ == "__main__":
    adaptee = Adaptee()
    print(adaptee.specific_request())  # Output: Request processed by Adaptee

    adapter = Adapter(adaptee)
    print(adapter.request())  # Output: Adapter: Request processed by Adaptee
