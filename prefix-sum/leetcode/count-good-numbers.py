class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(num,p):
            mod = p % 2
            if p == 0:
                return 1
            if p == 1:
                return num
            
            half = power(num,p//2) 
            res = half * half
            res = res % 1000000007
            return res*num if mod else res
        evens = (n//2) + (n%2)
        odds = n//2
        fours = power(4,odds)%1000000007
        fives = power(5,evens)%1000000007
        return (fours*fives)%1000000007