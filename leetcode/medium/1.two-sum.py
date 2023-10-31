#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            numMap[nums[i]] = i
        for i in range(n):
            comp = target - nums[i]
            if comp in numMap and numMap[comp] != i:
                return [i, numMap[comp]]


# @lc code=end
