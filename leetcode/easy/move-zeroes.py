// https://leetcode.com/problems/move-zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        return nums