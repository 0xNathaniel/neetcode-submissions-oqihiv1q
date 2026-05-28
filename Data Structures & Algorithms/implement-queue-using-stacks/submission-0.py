class MyQueue:

    def __init__(self):
        self.queue = []
        self.helper_queue = []

    def push(self, x: int) -> None:
        # Append to list in Python is equivalen to stack's push to top
        self.queue.append(x)

    def pop(self) -> int:
        while self.queue:
            # Python's list pop is equivalent to stack's pop of top
            item = self.queue.pop()
            self.helper_queue.append(item)
        if self.helper_queue:
            return_item = self.helper_queue.pop()
        
        while self.helper_queue:
            item = self.helper_queue.pop()
            self.queue.append(item)

        return return_item


    def peek(self) -> int:
        peek_queue = self.queue[:]
        while len(peek_queue) > 1:
            peek_queue.pop()
        return peek_queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()