class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        for i, item in enumerate(self.keys):
            if item == key:
                self.values[i] = value
                return
        self.keys.append(key)
        self.values.append(value)

    def get(self, key: int) -> int:
        for i, item in enumerate(self.keys):
            if item == key:
                return self.values[i]
        return -1

    def remove(self, key: int) -> None:
        for i, item in enumerate(self.keys):
            if item == key:
                self.keys.pop(i)
                self.values.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)