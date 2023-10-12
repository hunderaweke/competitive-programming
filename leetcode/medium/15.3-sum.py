#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, m, r = 0, len(nums) // 2, len(nums) - 1
        res = set()
        while l < m and m < r:
            s = nums[l] + nums[m] + nums[r]
            if s == 0:
                res.add((nums[l], nums[m], nums[r]))
                m -= 1
                l, r = 0, len(nums) - 1
            elif s > 0:
                r -= 1
            elif s < 0:
                l += 1
        res = list(res)
        return res


# @lc code=end
