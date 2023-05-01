from abc import ABC, abstractmethod


__all__ = [
    'Dog', 'Cat'
]


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        """
        Dog class implements the make_sound method from the Animal class.
        """
        return "Woof!"


class Cat(Animal):
    def make_sound(self) -> str:
        """
        Cat class implements the make_sound method from the Animal class.
        """
        return "Meow!"
