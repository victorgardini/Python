from abc import ABC, abstractmethod


class Implementor(ABC):
    """
    The Implementor interface declares methods common to all concrete
    implementors. It doesn't have to match the Abstraction's interface. In
    fact, the two interfaces can be entirely different. Typically the
    Implementor interface provides only primitive operations, while the
    Abstraction defines higher-level operations based on those primitives.
    """
    @abstractmethod
    def operation_implementation(self):
        pass


class ConcreteImplementorA(Implementor):
    """
    Each Concrete Implementor corresponds to a specific platform and implements
    the Implementor interface using that platform's API.
    """
    def operation_implementation(self) -> str:
        """
        ConcreteImplementorA implements the Implementor interface and defines
        its concrete implementation. This method could return some complex data
        type that is not necessarily a string.
        """
        return "ConcreteImplementorA: operation_implementation"


class ConcreteImplementorB(Implementor):
    """
    Each Concrete Implementor corresponds to a specific platform and implements
    the Implementor interface using that platform's API.
    """
    def operation_implementation(self) -> str:
        """
        ConcreteImplementorB implements the Implementor interface and defines
        its concrete implementation. The implementation can be different from
        the one in ConcreteImplementorA, but the interface has to be compatible
        so that the ConcreteAbstraction can work with any concrete implementor.
        """
        return "ConcreteImplementorB: operation_implementation"


class Abstraction:
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementor hierarchy and delegates all of the real work to this object.
    """
    def __init__(self, implementor: Implementor):
        """
        The Abstraction is usually initialized with one of the Implementor
        objects. The pattern doesn't preclude the Abstraction from working with
        multiple Implementors at once, but this is less common.
        """
        self.implementor = implementor

    def operation(self):
        """
        The Abstraction delegates some work to the Implementor object instead
        of doing everything on its own.
        """
        return f"Abstraction: Base operation with:\n{self.implementor.operation_implementation()}"


class RefinedAbstraction(Abstraction):
    """
    You can extend the Abstraction without changing the Implementor classes.
    """
    def operation(self):
        return f"RefinedAbstraction: Extended operation with:\n{self.implementor.operation_implementation()}"


if __name__ == "__main__":
    implementor_a = ConcreteImplementorA()  # Create an object of the ConcreteImplementorA class
    abstraction = Abstraction(implementor_a)  # Create an object of the Abstraction class
    # Output: Abstraction: Base operation with: ConcreteImplementorA: operation_implementation
    print(abstraction.operation())  # Call the operation method of the Abstraction class

    implementor_b = ConcreteImplementorB()  # Create an object of the ConcreteImplementorB class
    refined_abstraction = RefinedAbstraction(implementor_b)  # Create an object of the RefinedAbstraction class
    # Output: RefinedAbstraction: Extended operation with: ConcreteImplementorB: operation_implementation
    print(refined_abstraction.operation())  # Call the operation method of the RefinedAbstraction class
