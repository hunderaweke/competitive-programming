class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 100,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        stack = []
        interger = 0
        for n in s:
            stack.append(romans[n])
        while len(stack):
            num = stack.pop()
            if not stack:
                interger += num
            elif num <= stack[-1]:
                interger += num
            else:
                interger += num - stack.pop()
        return interger