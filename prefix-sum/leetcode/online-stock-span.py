class StockSpanner:

    def __init__(self):
        self.stack = []
        self.days = 0
    
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
            if self.stack:
                span = self.days - self.stack[-1][1]
            else:
                span = self.days + 1
        self.stack.append((price,self.days))
        self.days += 1
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)