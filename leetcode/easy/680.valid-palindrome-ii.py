#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                s1 = s[:l] + s[l + 1 :]
                s2 = s[:r] + s[r + 1 :]
                return s1 == s1[::-1] or s2 == s2[::-1]
            l += 1
            r -= 1
        return True


# @lc code=end
