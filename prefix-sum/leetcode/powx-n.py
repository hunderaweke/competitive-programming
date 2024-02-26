class Solution:
    def myPow(self, x: float, n: int) -> float:
        mod = abs(n)%2
        if n == 0:
            return 1
        power = self.myPow(x,abs(n)//2)
        if n  > 0:
            return power*power*x**mod
        return 1/(power*power*x**mod)