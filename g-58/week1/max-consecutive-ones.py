class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for num in nums:
            if num != 1:
                ans = max(ans,count)   
                count = 0
            else:
                count += 1
        return max(ans,count)
            