#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = sorted(nums)
        dic = dict()
        for i in nums:
            if i not in dic:
                dic[i] = n.index(i)
            else:
                continue
        res = [dic[i] for i in nums]
        return res
# @lc code=end

