class FrequencyTracker:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.frefre = defaultdict(int)
    def add(self, number: int) -> None:
        self.frequency[number] += 1
        self.frefre[self.frequency[number]] += 1
        self.frefre[self.frequency[number] - 1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.frequency[number]:
            self.frequency[number] -= 1
            if not self.frequency[number]:
                self.frequency.pop(number)
            self.frefre[self.frequency[number]] += 1
            self.frefre[self.frequency[number] + 1] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frefre[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)