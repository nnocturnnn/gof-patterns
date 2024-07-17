from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass


class DarkButton(Button):
    def paint(self) -> str:
        return "Dark Button"


class LightButton(Button):
    def paint(self) -> str:
        return "Light Button"


class BlueButton(Button):
    def paint(self) -> str:
        return "Blue Button"


class ButtonFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass


class DarkButtonFactory(ButtonFactory):
    def create_button(self) -> DarkButton:
        return DarkButton()


class LightButtonFactory(ButtonFactory):
    def create_button(self) -> LightButton:
        return LightButton()


class BlueButtonFactory(ButtonFactory):
    def create_button(self) -> BlueButton:
        return BlueButton()


class Application:
    def __init__(self, factory: ButtonFactory) -> None:
        self.factory = factory.create_button()

    def paint(self) -> str:
        return self.factory.paint()


if __name__ == "__main__":
    theme = "dark"
    factory: ButtonFactory = (
        DarkButtonFactory() if theme == "dark" else LightButtonFactory()
    )
    app = Application(factory)
    print(app.paint())
