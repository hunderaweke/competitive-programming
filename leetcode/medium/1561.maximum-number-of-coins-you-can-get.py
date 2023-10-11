#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count =0
        left = 0
        right = len(piles)-2
        while left<right:
            count += piles[right]
            right -=2
            left +=1
        return count
        
# @lc code=end

