class Solution:
    def fib(self, n: int) -> int:
        c1,c2 = (5**0.5)/5,-(5**0.5)/5
        r1,r2 = (1+(5**0.5))/2,(1-(5**0.5))/2
        return int((c1*r1**n) + (c2*r2**n))