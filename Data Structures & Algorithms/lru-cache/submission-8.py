class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value = self.cache.pop(key)
        self.cache[key] = value
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        if len(self.cache) == self.capacity:
            lru = next(iter(self.cache))
            self.cache.pop(lru)

        self.cache[key] = value