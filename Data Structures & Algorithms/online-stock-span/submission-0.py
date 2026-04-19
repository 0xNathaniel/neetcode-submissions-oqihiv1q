class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)

        temp_stack = self.stack.copy()
        count = 0
        while temp_stack and temp_stack[-1] <= price:
            count += 1
            temp_stack.pop()

        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)