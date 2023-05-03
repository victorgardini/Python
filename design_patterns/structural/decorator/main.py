# Decorator is a structural design pattern that lets you attach new behaviors to objects by placing
# these objects inside special wrapper objects that contain the behaviors.

from abc import ABC, abstractmethod


class Component(ABC):
    """
    The base Component interface defines operations that can be altered by decorators.
    """
    @abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations.
    There might be several variations of these classes.
    """
    def operation(self):
        """
        Concrete Components may have some interesting default implementation of the operation.
        """
        return "ConcreteComponent"


class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for all concrete decorators.
    The default implementation of the wrapping code might include a field for storing a wrapped component
    and the means to initialize it.
    """
    def __init__(self, component: Component):
        self._component = component

    @abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):
    """
    Decorators may call parent implementation of the operation, instead of calling the wrapped object directly.
    This approach simplifies extension of decorator classes.
    """
    def operation(self):
        # You can add some behavior here, like logging. Then you can call the parent
        # implementation of the operation.
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"


if __name__ == "__main__":
    component = ConcreteComponent()
    decorator1 = ConcreteDecoratorA(component)
    decorator2 = ConcreteDecoratorB(decorator1)

    print(decorator2.operation())
