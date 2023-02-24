from functools import wraps


def raise_data_is_none(class_method):
    """
    This decorator is to be used on LinkedList methods, to raise an exception if the data is None.
    """
    @wraps(class_method)
    def wrapper(self, data):
        if data is None:
            raise TypeError("Data cannot be None")
        return class_method(self, data)
    return wrapper
