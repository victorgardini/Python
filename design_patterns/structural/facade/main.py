# Facade is a structural design pattern that provides a simplified interface to a library,
# a framework, or any other complex set of classes.

from typing import Optional


class SubsystemA:
    """
    The Subsystem can accept requests either from the facade or client directly.
    """
    def operation_1(self):
        # some logic
        return "SubsystemA method1"

    def operation_2(self):
        return "SubsystemA method2"


class SubsystemB:
    def operation_1(self):
        return "SubsystemB method1"

    def operation_2(self):
        return "SubsystemB method2"


class SubsystemC:
    def operation_1(self):
        return "SubsystemC method1"

    def operation_2(self):
        return "SubsystemC method2"


class Facade:
    """
    The Facade class provides a simple interface to the complex logic of one or
    several subsystems. The Facade delegates the client requests to the
    appropriate objects within the subsystem. The Facade is also responsible for
    managing their lifecycle. All of this shields the client from the undesired
    complexity of the subsystem.
    """

    def __init__(
            self,
            subsystem_a: Optional[SubsystemA] = None,
            subsystem_b: Optional[SubsystemB] = None,
            subsystem_c: Optional[SubsystemC] = None
    ):
        """
        Depending on your application's needs, you can provide the Facade with
        existing subsystem objects or force the Facade to create them on its
        own.
        """
        self._subsystem_a = subsystem_a or SubsystemA()
        self._subsystem_b = subsystem_b or SubsystemB()
        self._subsystem_c = subsystem_c or SubsystemC()

    def operation(self) -> str:
        """
        The Facade's methods are convenient shortcuts to the sophisticated
        functionality of the subsystems. However, clients get only to a fraction
        of a subsystem's capabilities.
        """
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem_a.operation_1())
        results.append(self._subsystem_b.operation_1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem_a.operation_1())
        results.append(self._subsystem_b.operation_2())
        return "\n".join(results)


if __name__ == "__main__":
    subsystem1 = SubsystemA()
    subsystem2 = SubsystemB()

    facade = Facade(subsystem1, subsystem2)  # initialize subsystems is optional
    result = facade.operation()

    print(result)
