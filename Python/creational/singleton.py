from typing import Any, Dict


class SingletonBaseClass(type):
    _instances: Dict[type, Any] = {}

    def __call__(cls: type, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBaseClass, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]


class Singleton(metaclass=SingletonBaseClass):
    def __init__(self, name: str) -> None:
        self.name: str = name

    def __str__(self) -> str:
        return self.name
