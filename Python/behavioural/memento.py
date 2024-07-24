class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class API:
    def __init__(self, url):
        self._url = url

    def get_url(self):
        return self._url

    def set_url(self, url):
        self._url = url

    def save(self):
        return Memento(self._url)

    def restore(self, memento):
        self._url = memento.get_state()


class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


if __name__ == "__main__":
    api = API("https://www.google.com")
    caretaker = Caretaker()

    caretaker.add_memento(api.save())
    print(api.get_url())

    api.set_url("https://www.google.com/search?q=python")
    print(api.get_url())

    api.restore(caretaker.get_memento(0))
    print(api.get_url())
