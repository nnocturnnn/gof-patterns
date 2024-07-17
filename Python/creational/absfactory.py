from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class DarkButton(Button):
    def paint(self):
        return "Dark Button"


class LightButton(Button):
    def paint(self):
        return "Light Button"


class BlueButton(Button):
    def paint(self):
        return "Blue Button"


class ButtonFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass


class DarkButtonFactory(ButtonFactory):
    def create_button(self):
        return DarkButton()


class LightButtonFactory(ButtonFactory):
    def create_button(self):
        return LightButton()


class BlueButtonFactory(ButtonFactory):
    def create_button(self):
        return BlueButton()


class Application:
    def __init__(self, factory):
        self.factory = factory.create_button()

    def paint(self):
        return self.factory.paint()


if __name__ == "__main__":
    theme = "dark"
    factory = DarkButtonFactory() if theme == "dark" else LightButtonFactory()
    app = Application(factory)
    app.paint()
