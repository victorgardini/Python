from typing import Optional


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size: int = 100):
        self.size = size
        self.slots = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def set(self, key, value) -> None:
        hash_index = self._hash(key)

        for item in self.slots[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.slots[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash(key)

        for item in self.slots[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError(f"Key {key} not found")

    def delete(self, key) -> None:
        hash_index = self._hash(key)

        for index, item in enumerate(self.slots[hash_index]):
            if item.key == key:
                del self.slots[hash_index][index]
                return
        raise KeyError(f"Key {key} not found")

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __delitem__(self, key):
        return self.delete(key)

    def __repr__(self):
        return f'HashTable(size={self.size}, slots={self.slots})'

    def __str__(self):
        return str(self.slots)
