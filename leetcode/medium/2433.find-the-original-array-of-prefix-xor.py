#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#


# @lc code=start
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        res.append(pref[0])
        for i in range(1,len(pref)):
            res.append(pref[i]^pref[i-1])
        return res


# @lc code=end
