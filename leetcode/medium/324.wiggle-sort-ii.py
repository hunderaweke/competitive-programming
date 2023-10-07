#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])-1
        nums[::2],nums[1::2] = nums[half::-1],nums[:half:-1]
# @lc code=end

