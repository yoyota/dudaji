# get, set, remove
# hash_function, key linear search in bucket


class HashTable:
    def __init__(self, capacity=256):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def __len__(self):
        return self.size

    def hash_fn(self, key):
        hash = 0

        for i in key:
            hash = hash * 31 + ord(i)
        return hash % self.capacity

    def _find_bucket(self, key):
        index = self.hash_fn(key)
        return self.buckets[index]

    def _find(self, key):
        bucket = self._find_bucket(key)
        for item in bucket:
            if item[0] == key:
                return bucket, item
        return bucket, None

    def set(self, key, value):
        if not isinstance(key, str):
            raise KeyError(key)
        bucket, box = self._find(key)
        if not box:
            bucket.append([key, value])
            self.size += 1
            return
        box[1] = value

    def get(self, key):
        _, box = self._find(key)
        if not box:
            raise KeyError(key)
        return box[1]

    def remove(self, key):
        _, box = self._find(key)
        if not box:
            raise KeyError(key)
        value = box[1]
        del box
        self.size -= 1
        return value
