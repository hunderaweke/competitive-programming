#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,b = nums.count(0),nums.count(1)
        for i in range(len(nums)):
            if a>0:
                nums[i] = 0
                a-=1
            elif b>0:
                nums[i] = 1
                b-=1
            else:
                nums[i] = 2
# @lc code=end

