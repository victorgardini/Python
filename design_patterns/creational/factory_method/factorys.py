# factorys.py file implements the factory method pattern using abstract classes.

from abc import ABC, abstractmethod
from animals import Dog, Cat


__all__ = [
    'DogFactory', 'CatFactory'
]


class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass


class DogFactory(AnimalFactory):
    def create_animal(self) -> Dog:
        """
        DogFactory class implements the create_animal method from the AnimalFactory class.
        """
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self) -> Cat:
        """
        CatFactory class implements the create_animal method from the AnimalFactory class.
        """
        return Cat()
