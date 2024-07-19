from abc import ABC, abstractmethod

class CacheFlyweight(ABC):
    @abstractmethod
    def get_data(self, query: str):
        pass


class ConcreteCacheFlyweight(CacheFlyweight):
    def __init__(self):
        self.cache = {}

    def get_data(self, query: str):
        if query in self.cache:
            print(f"Cache hit for query: {query}")
            return self.cache[query]
        else:
            print(f"Cache miss for query: {query}")
            data = self.fetch_data_from_db(query)
            self.cache[query] = data
            return data

    def fetch_data_from_db(self, query: str):
        return f"Data for {query}"


class CacheFlyweightFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, key: str):
        if key not in cls._flyweights:
            cls._flyweights[key] = ConcreteCacheFlyweight()
        return cls._flyweights[key]


if __name__ == "__main__":
    flyweight = CacheFlyweightFactory.get_flyweight("key")
    print(flyweight.get_data("query1"))
    print(flyweight.get_data("query2"))

    flyweight = CacheFlyweightFactory.get_flyweight("another key")
    print(flyweight.get_data("query1"))
    print(flyweight.get_data("query2"))