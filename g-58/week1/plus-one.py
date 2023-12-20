class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(x) for x in digits]
        num = int(''.join(digits))
        num +=1
        num = str(num)
        return [int(x) for x in num]