#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#


# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        ans = 1

        def cmp(a, b):
            return (a > b) - (a < b)

        for right in range(1, n):
            c = cmp(arr[right - 1], arr[right])
            if c == 0:
                left = right
            elif right == n - 1 or c * cmp(arr[right], arr[right + 1]) != -1:
                ans = max(ans, right - left + 1)
                left = right
        return ans


# @lc code=end
