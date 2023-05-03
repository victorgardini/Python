# Composite is a structural design pattern that allows composing objects into a tree-like structure
# and work with the it as if it was a singular object.

from abc import ABC, abstractmethod


class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """
    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):
    """
    You can extend the Leaf class as long as you don't change the Component's
    interface.
    """
    def operation(self):
        """
        The method operation of the Leaf class does not contain a call to the
        parent's method. Because the leaf does not have a parent.
        """
        return "Leaf operation"


class Composite(Component):
    """
    The Composite's method operation imitates the behavior of the Leaf's one.
    The Composite executes its primary logic in a particular way. It traverses
    recursively through all its children, collecting and summing their results.
    """
    def __init__(self):
        self.children = []

    def add(self, component: Component):
        """
        A composite object can add or remove other components (both simple or
        complex) to or from its child list.
        """
        self.children.append(component)

    def remove(self, component: Component):
        self.children.remove(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Composite operation:\n{' '.join(results)}"


if __name__ == "__main__":
    leaf1 = Leaf()
    leaf2 = Leaf()
    leaf3 = Leaf()

    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)
    composite.add(leaf3)

    composite2 = Composite()
    composite2.add(leaf1)
    composite2.add(leaf2)

    composite.add(composite2)

    print(composite.operation())

