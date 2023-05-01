"""
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.
"""

from factorys import DogFactory, CatFactory


if __name__ == "__main__":
    dog_factory = DogFactory()
    cat_factory = CatFactory()

    dog = dog_factory.create_animal()
    cat = cat_factory.create_animal()

    dog.make_sound()  # returns "Woof!" string
    cat.make_sound()  # returns "Meow!" string
