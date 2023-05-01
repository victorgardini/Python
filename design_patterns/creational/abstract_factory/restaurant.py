from abc import ABC, abstractmethod

from beverage import Coke, Pepsi
from pizza import Margherita, Pepperoni


__all__ = ["ItalianRestaurant", "AmericanRestaurant"]


# Abstract Factory
class Restaurant(ABC):
    """ Abstract Factory """
    @abstractmethod
    def get_pizza(self):
        """ Abstract Factory Method """
        pass

    @abstractmethod
    def get_beverage(self):
        """ Abstract Factory Method """
        pass


# Concrete Factory 1
class ItalianRestaurant(Restaurant):
    def get_pizza(self):
        """
        Concrete Factory Method: Returns a Concrete Product A1
        """
        return Margherita()

    def get_beverage(self):
        """
        Concrete Factory Method: Returns a Concrete Product B1
        """
        return Coke()


# Concrete Factory 2
class AmericanRestaurant(Restaurant):
    def get_pizza(self):
        """
        Concrete Factory Method: Returns a Concrete Product A2
        """
        return Pepperoni()

    def get_beverage(self):
        """
        Concrete Factory Method: Returns a Concrete Product B2
        """
        return Pepsi()
