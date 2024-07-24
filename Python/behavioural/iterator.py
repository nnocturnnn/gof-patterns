class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            result = self._collection[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Collection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return Iterator(self._items)


collection = Collection()
collection.add_item(1)
collection.add_item(2)
collection.add_item(3)

for item in collection:
    print(item)
