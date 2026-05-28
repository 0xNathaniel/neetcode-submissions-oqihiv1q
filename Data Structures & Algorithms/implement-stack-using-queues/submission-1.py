class MyStack:

    def __init__(self):
        self.queue = []
        self.helper_queue = []

    def push(self, x: int) -> None:
        if self.queue:
            self.queue.append(x)
        else:
            self.helper_queue.append(x)

    def pop(self) -> int:
        if not self.helper_queue:
            while len(self.queue) > 1:
                self.helper_queue.append(self.queue.pop(0))
            return self.queue.pop()
        elif not self.queue: 
            while len(self.helper_queue) > 1:
                self.queue.append(self.helper_queue.pop(0))
            return self.helper_queue.pop()

    def top(self) -> int:
        if not self.helper_queue:
            while len(self.queue) > 1:
                self.helper_queue.append(self.queue.pop(0))
            res = self.queue[0]
            self.helper_queue.append(self.queue.pop())
            return res
        elif not self.queue: 
            while len(self.helper_queue) > 1:
                self.queue.append(self.helper_queue.pop(0))
            res = self.helper_queue[0]
            self.queue.append(self.helper_queue.pop())
            return res

    def empty(self) -> bool:
        return len(self.queue) == len(self.helper_queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()