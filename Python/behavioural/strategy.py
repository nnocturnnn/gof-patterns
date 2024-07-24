import json


class CacheStrategy:
    def store(self, data):
        pass

    def retrieve(self, key):
        pass


class MemoryCacheStrategy(CacheStrategy):
    def __init__(self):
        self.cache = {}

    def store(self, key, data):
        self.cache[key] = data
        print(f"Data stored in memory cache: {key}")

    def retrieve(self, key):
        return self.cache.get(key, "Data not found in memory cache")


class DiskCacheStrategy(CacheStrategy):
    def __init__(self, filename):
        self.filename = filename
        self.cache = self._load_cache()

    def _load_cache(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_cache(self):
        with open(self.filename, "w") as file:
            json.dump(self.cache, file)

    def store(self, key, data):
        self.cache[key] = data
        self._save_cache()
        print(f"Data stored in disk cache: {key}")

    def retrieve(self, key):
        return self.cache.get(key, "Data not found in disk cache")


class CacheContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def store_data(self, key, data):
        self.strategy.store(key, data)

    def retrieve_data(self, key):
        return self.strategy.retrieve(key)


memory_cache = MemoryCacheStrategy()
disk_cache = DiskCacheStrategy("cache.json")

cache = CacheContext(memory_cache)
cache.store_data("example", "Data for memory cache")
print(cache.retrieve_data("example"))

cache.set_strategy(disk_cache)
cache.store_data("example", "Data for disk cache")
print(cache.retrieve_data("example"))
