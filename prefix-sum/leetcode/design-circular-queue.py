class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.inserted = 0
        self.front = 0
        self.queue = []

    def enQueue(self, value: int) -> bool:
        if self.inserted >= self.space:
            return False
        self.queue.append(value)
        self.inserted += 1
        return True

    def deQueue(self) -> bool:
        if not self.inserted:
            return False
        self.front += 1
        self.inserted -= 1
        return True

    def Front(self) -> int:
        if self.inserted == 0:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.inserted == 0:
            return -1
        print(self.queue)
        return self.queue[-1]

    def isEmpty(self) -> bool:
        return not self.inserted

    def isFull(self) -> bool:
        return self.inserted == self.space


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()