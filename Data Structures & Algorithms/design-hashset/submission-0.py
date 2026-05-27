class MyHashSet:

    def __init__(self):
        self.items = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.items.append(key)

    def remove(self, key: int) -> None:
        for i, item in enumerate(self.items):
            if item == key:
                self.items.pop(i)

    def contains(self, key: int) -> bool:
        for item in self.items:
            if item == key:
                return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)