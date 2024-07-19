from abc import ABC, abstractmethod

class IObserver(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class ISubject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class Article(ISubject):
    def __init__(self, title, content):
        self._title = title
        self._content = content
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    def publish(self):
        print(f"Article '{self._title}' is published.")
        self.notify()

class EmailNotificationObserver(IObserver):
    def update(self, subject):
        print(f"Sending email: The article '{subject.title}' has been published.")

class LogObserver(IObserver):
    def update(self, subject):
        print(f"Log entry: The article '{subject.title}' has been published.")

class CacheUpdateObserver(IObserver):
    def update(self, subject):
        print(f"Cache update: The article '{subject.title}' has been updated in the cache.")


if __name__ == "__main__":
    article = Article("Observer Pattern", "Design Patterns: Observer")
    article.attach(EmailNotificationObserver())
    article.attach(LogObserver())
    article.attach(CacheUpdateObserver())

    article.publish()