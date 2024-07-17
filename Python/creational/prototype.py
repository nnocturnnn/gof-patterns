import copy
from typing import Any, Dict


class Prototype:
    def __init__(self) -> None:
        self._objects: Dict[str, Any] = {}

    def register_object(self, name: str, obj: Any) -> None:
        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        if name in self._objects:
            del self._objects[name]

    def clone(self, name: str, **attr: Any) -> Any:
        obj = copy.deepcopy(self._objects.get(name))
        if obj is not None:
            obj.__dict__.update(attr)
        return obj
