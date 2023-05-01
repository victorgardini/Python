class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_wheels()
        self._builder.add_engine()
        self._builder.add_body()

    def get_car(self):
        return self._builder.car


class Builder:
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """
    def __init__(self):
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.car = None

    def create_new_car(self):
        """
        Create a blank product object.
        """
        self.car = Car()


class Car:
    def __init__(self):
        self.wheels = None
        self.engine = None
        self.body = None

    def __str__(self):
        return f"Wheels: {self.wheels}, Engine: {self.engine}, Body: {self.body}"


class JeepBuilder(Builder):
    def add_wheels(self):
        self.car.wheels = "Large Wheels"

    def add_engine(self):
        self.car.engine = "Powerful Engine"

    def add_body(self):
        self.car.body = "SUV Body"


class SportsCarBuilder(Builder):
    def add_wheels(self):
        self.car.wheels = "Sport Wheels"

    def add_engine(self):
        self.car.engine = "Fast Engine"

    def add_body(self):
        self.car.body = "Sports Body"


if __name__ == "__main__":
    jeep_builder = JeepBuilder()
    director = Director(jeep_builder)
    director.construct_car()
    car = director.get_car()
    print(car)  # Output: Wheels: Large Wheels, Engine: Powerful Engine, Body: SUV Body

    sports_car_builder = SportsCarBuilder()
    director = Director(sports_car_builder)
    director.construct_car()
    car = director.get_car()
    print(car)  # Output: Wheels: Sport Wheels, Engine: Fast Engine, Body: Sports Body
