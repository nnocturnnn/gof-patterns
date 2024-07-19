from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_button(self, element):
        pass

    @abstractmethod
    def visit_text(self, element):
        pass

class AnalyticsVisitor(Visitor):
    def visit_button(self, element):
        print(f"Tracking analytics for button: {element.name}")

    def visit_text(self, element):
        print(f"Tracking analytics for text: {element.content}")

class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

class Button(Element):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor: Visitor):
        visitor.visit_button(self)

class Text(Element):
    def __init__(self, content):
        self.content = content

    def accept(self, visitor: Visitor):
        visitor.visit_text(self)

button = Button("Submit")
text = Text("Welcome to our site")

analytics = AnalyticsVisitor()
button.accept(analytics)
text.accept(analytics)
