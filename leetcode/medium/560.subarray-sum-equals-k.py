#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        res  =0
        preSum = 0
        for i in range(len(nums)):
            preSum += nums[i]
            if preSum -k  in d:
                res+=d[preSum-k]
            d[preSum] = d.get(preSum,0)+1
        return res
# @lc code=end

