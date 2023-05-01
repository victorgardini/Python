from abc import ABC, abstractmethod


__all__ = ["Coke", "Pepsi"]


# Abstract Product B
class Beverage(ABC):
    """
    Abstract Product B
    """
    @abstractmethod
    def serve(self):
        """
        Abstract method to serve a beverage
        """
        pass


# Concrete Product B1
class Coke(Beverage):
    """
    Concrete Product B1
    """
    def serve(self):
        """
        Concrete method to serve a Coke
        """
        return "Serving Coke"


# Concrete Product B2
class Pepsi(Beverage):
    """
    Concrete Product B2
    """
    def serve(self):
        """
        Concrete method to serve a Pepsi
        """
        return "Serving Pepsi"
