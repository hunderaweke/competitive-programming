#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = dict(Counter(s))
        counter = sorted(counter.items(),key=lambda x:x[1],reverse=True)
        counter  = dict(counter)
        res = ''
        for i in counter:
            while counter[i] != 0:
                res += i
                counter[i] -=1
        return res
# @lc code=end

