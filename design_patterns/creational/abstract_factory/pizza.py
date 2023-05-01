from abc import ABC, abstractmethod


__all__ = ["Margherita", "Pepperoni"]


# Abstract Product A
class Pizza(ABC):
    """
    Abstract Product A
    """
    @abstractmethod
    def prepare(self):
        """
        Abstract method to prepare pizza
        """
        pass


# Concrete Product A1
class Margherita(Pizza):
    def prepare(self):
        """
        Concrete method to prepare Margherita pizza
        """
        return "Preparing Margherita Pizza"


# Concrete Product A2
class Pepperoni(Pizza):
    def prepare(self):
        """
        Concrete method to prepare Pepperoni pizza
        """
        return "Preparing Pepperoni Pizza"
