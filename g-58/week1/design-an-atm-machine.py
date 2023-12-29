class ATM:

    def __init__(self):
        self.bankNotes = [20,50,100,200,500]
        self.bank = [0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i,count in enumerate(banknotesCount):
            self.bank[i] += count

    def withdraw(self, amount: int) -> List[int]:
        withdraw =[0]*5
        for i in reversed(range(5)):
            withdraw[i] = min(self.bank[i],amount//self.bankNotes[i])
            amount -= withdraw[i] * self.bankNotes[i]
        if amount:
            return [-1]
        for i in range(5):
            self.bank[i] -= withdraw[i]
        return withdraw

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)