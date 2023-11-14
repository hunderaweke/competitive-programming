class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c))+1):
            b = c - (a*a) 
            b = sqrt(b)
            if b == int(b):
                return True
        return False
