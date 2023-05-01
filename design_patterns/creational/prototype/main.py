import copy
from dataclasses import dataclass


@dataclass
class Car:
    """
    The Car class has a constructor that accepts a model name and fuel consumption.
    """
    id: int
    name: str
    color: str
    year: int


class Prototype:
    """
    The Prototype class declares the cloning interface.
    """
    def __init__(self):
        self._objects = {}  # Initialize the objects dictionary

    def register(self, new_car: 'Car'):
        """
        Register a new object in the dictionary
        """
        obj = self._objects.get(new_car.id)
        if obj is None:
            obj = self._objects[new_car.id] = new_car
        return obj

    @staticmethod
    def _create_object(**kwargs) -> 'Car':
        """
        Create a new car object
        """
        return Car(**kwargs)

    def register_object(self, name, obj):
        self._objects[name] = obj  # Save into the dictionary the object passed as parameter

    def unregister_object(self, name):
        del self._objects[name]  # Delete the object from the dictionary

    def clone(self, card_id, **kwargs):
        # Get the object from the dictionary and make a deep copy of it
        cloned_obj = copy.deepcopy(
            self._objects.get(card_id)
        )
        # Update the cloned object with the new values
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


if __name__ == "__main__":
    car = Car(id=1, name='Ferrari', color="red", year=2019)  # Create a new car

    prototype = Prototype()  # Create a prototype to clone the car
    prototype.register_object(1, car)  # Register the car into the prototype

    cloned_car = prototype.clone(1, color="Blue", name="Ferrari 488 GTB")  # Clone the car and update the values
    print(cloned_car)  # Output: {'id': 1, 'name': 'Ferrari', 'color': 'Blue', 'year': 2019}
