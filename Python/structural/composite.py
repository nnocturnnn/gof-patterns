from abc import ABC, abstractmethod


class ModuleComponent(ABC):
    @abstractmethod
    def add(self, module: "ModuleComponent"):
        pass

    @abstractmethod
    def remove(self, module: "ModuleComponent"):
        pass

    @abstractmethod
    def display(self, depth: int):
        pass


class Module(ModuleComponent):
    def __init__(self, name: str):
        self.name = name

    def add(self, module: "ModuleComponent"):
        raise NotImplementedError("Cannot add to a leaf")

    def remove(self, module: "ModuleComponent"):
        raise NotImplementedError("Cannot remove from a leaf")

    def display(self, depth: int):
        print(f"{'-' * depth} {self.name}")


class CompositeModule(ModuleComponent):
    def __init__(self, name: str):
        self.name = name
        self.modules = []

    def add(self, module: "ModuleComponent"):
        self.modules.append(module)

    def remove(self, module: "ModuleComponent"):
        self.modules.remove(module)

    def display(self, depth: int):
        print(f"{'-' * depth} {self.name}")
        for module in self.modules:
            module.display(depth + 2)


if __name__ == "__main__":
    leaf1 = Module("Leaf 1")
    leaf2 = Module("Leaf 2")
    leaf3 = Module("Leaf 3")

    composite1 = CompositeModule("Composite 1")
    composite1.add(leaf1)
    composite1.add(leaf2)

    composite2 = CompositeModule("Composite 2")
    composite2.add(composite1)
    composite2.add(leaf3)

    composite2.display(1)
