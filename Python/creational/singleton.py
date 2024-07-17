class SingletonBaseClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBaseClass, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]


class Singleton(metaclass=SingletonBaseClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
