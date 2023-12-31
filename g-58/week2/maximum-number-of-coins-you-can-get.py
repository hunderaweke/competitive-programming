class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans =0 
        left,right = 0,len(piles)-2
        while left < right:
            ans += piles[right]
            right -= 2
            left += 1
        return ans
