class Singleton:
    """
    Implementation of SingleTon pattern, which is used to create only one instance of a class.
    """
    _instance = None

    def __new__(cls):
        """
        This method is called when an object is created from a class and it allows the
        class to control the creation of the object.
        """
        if cls._instance is None:  # If the class has no instance
            cls._instance = super().__new__(cls)  # create an object of the class
        return cls._instance  # return the object of the class


if __name__ == "__main__":
    singleton1 = Singleton()  # Create an object of the class
    singleton2 = Singleton()  # Create another object of the class

    print(singleton1 is singleton2)  # Output: True (Both objects are the same)
